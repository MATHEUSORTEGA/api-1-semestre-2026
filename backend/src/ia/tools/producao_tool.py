# Funções para estimativa de produção.
# Função para TOOLS do DSPY relacionadas a produção.
import math
import sys
from pathlib import Path

import pandas as pd

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from ia.procedures import procedures
from ia.tools.utils import dspy_tool


def media_vendas_produtos(vendas, setor=None):
    """
    Calcula a média de vendas de cada produto e arredonda o resultado
    para cima.

    Args:
        vendas (list): Lista de vendas no formato de registros
            de um DataFrame do pandas.
        setor (str, opcional): Setor utilizado para filtrar os produtos.
            Se não for informado, calcula a média de todos os produtos.

    Returns:
        list: Lista contendo o nome de cada produto e sua média
            de vendas arredondada para cima.

            Exemplo:
            ['Brigadeiro: 4', 'Temaki: 7', 'Pão Francês: 4']
    """

    dados = pd.DataFrame(vendas)

    if setor is not None:
        produtos_setor = procedures.produtos.buscar_por_setor(setor)

        nomes_produtos = [
            produto["Produto"]
            for produto in produtos_setor
        ]

        dados = dados[
            dados["Produto"].isin(nomes_produtos)
        ]

    medias = dados.groupby("Produto")["Qtd"].mean()

    resultado = []

    for produto, media in medias.items():
        media_arredondada = math.ceil(media)

        resultado.append(
            f"{produto}: {media_arredondada}"
        )

    return resultado


@dspy_tool
def estimativa_producao_passado(data: str, setor: str) -> str:
    """Estima quanto deveria ser produzido em um dia passado para um setor.

    Use esta ferramenta quando o gerente informar uma data específica no
    passado e quiser saber a produção recomendada de cada produto de um setor.
    O parâmetro ``data`` deve estar no formato ``DD/MM/AAAA`` e ``setor`` deve
    conter o nome do setor, como "Padaria" ou "Confeitaria".

    Use: python -c "from ia.tools.producao_tool import estimativa_producao_passado; print(estimativa_producao_passado('DD/MM/AAAA', 'SETOR'))"

    Args:
        data: Data do dia que será estimado, no formato ``DD/MM/AAAA``.
        setor: Setor dos produtos que devem ser incluídos na estimativa.

    Returns:
        Uma string com a estimativa de produção de cada produto, ou uma
        mensagem informando que não há vendas anteriores para a consulta.
    """
    try:
        data_alvo = pd.to_datetime(data, format="%d/%m/%Y")
    except (TypeError, ValueError) as erro:
        raise ValueError(
            "A data deve estar no formato DD/MM/AAAA."
        ) from erro

    vendas = procedures.vendas.todas_as_vendas().copy()
    vendas["Data"] = pd.to_datetime(
        vendas["Data"],
        format="%d/%m/%Y",
    )
    vendas_anteriores = vendas[vendas["Data"] < data_alvo]

    if vendas_anteriores.empty:
        return "Não há vendas anteriores à data informada para calcular a estimativa."

    vendas_anteriores = vendas_anteriores.assign(
        Data=vendas_anteriores["Data"].dt.strftime("%d/%m/%Y")
    )
    estimativas = media_vendas_produtos(vendas_anteriores.to_dict("records"), setor)

    if not estimativas:
        return f"Não há vendas anteriores para o setor '{setor}'."

    return "\n".join(estimativas)