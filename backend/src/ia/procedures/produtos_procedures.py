from pathlib import Path
import pandas as pd

path = Path(__file__).resolve().parents[3] / "dados" / "produtos_mercado.csv"

def buscar_por_nome_produto(nome_produto: str):
    df = pd.read_csv(path)

    resultado = df[df['Nome'].str.contains(nome_produto, case=False, na=False)]

    return resultado.to_dict(orient='records')

def produto_por_setor(setor: str):
    df = pd.read_csv(path, sep=";", encoding="utf-8")

    resultado = df[df['Setor'].str.contains(setor, case=False, na=False)]

    return resultado.to_dict(orient='records')

print(produto_por_setor("Padaria"))