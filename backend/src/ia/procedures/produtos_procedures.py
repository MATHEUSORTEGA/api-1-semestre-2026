# procedures.vendas.buscar_por_nome_produto()
import pandas as pd

def buscar_por_nome_produto(nome_produto: str):
    """Busca um produto pelo nome."""
    df = pd.read_csv('../dados/produtos.csv')

    resultado = df[df['nome'].str.contains(nome_produto, case=False, na=False)]

    return resultado.to_dict(orient='records')
    