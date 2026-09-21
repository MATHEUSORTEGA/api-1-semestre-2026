from pathlib import Path
import pandas as pd

path = Path(__file__).resolve().parents[3] / "dados" / "produtos_mercado.csv"
prod_tb = pd.read_csv(path, sep=';')

def listar():
    produtos = prod_tb['Produto'].unique().tolist()
    print(f'[DEBUG] Produtos disponíveis: \n{produtos}')  
    return produtos

def buscar_por_nome_produto(nome_produto: str):
    df = pd.read_csv(path)

    resultado = df[df['Nome'].str.contains(nome_produto, case=False, na=False)]

    return resultado.to_dict(orient='records')

def produto_por_setor(setor: str):
    df = pd.read_csv(path, sep=";", encoding="utf-8")

    resultado = df[df['Setor'].str.contains(setor, case=False, na=False)]

def listar_detalhado() -> str:
    return prod_tb.to_string(index=False)

def buscar_por_nome(nome_produto: str):
    resultado = prod_tb[prod_tb['Produto'].str.contains(nome_produto, case=False, na=False)]
    print(f'[DEBUG] Resultado da busca por nome do produto: {resultado}')
    return resultado.to_dict(orient='records')

def buscar_por_setor(setor: str):
    resultado = prod_tb[prod_tb['Setor'].str.contains(setor, case=False, na=False)]
    print(f'[DEBUG] Resultado da busca por setor: {resultado}')
    return resultado.to_dict(orient='records')

def buscar_por_tempo(tempo: str):
    resultado = prod_tb[prod_tb['Tempo de preparo'].str.contains(tempo, case=False, na=False)]
    print(f'[DEBUG] Resultado da busca por tempo de preparo: {resultado}')
    return resultado.to_dict(orient='records')
