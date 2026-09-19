from pathlib import Path
import pandas as pd
path1 = Path(__file__).resolve().parents[3] / "dados" / "vendas_supermercado_agosto_2026.csv"
path2 = Path(__file__).resolve().parents[3] / "dados" / "vendas_supermercado_setembro_2026.csv"
vsa, vss = pd.read_csv(path1, sep=";"), pd.read_csv(path2, sep=";")
tabela = pd.concat([vsa, vss], ignore_index=True)

def buscar_por_nome_produto(nome):
    return tabela[tabela["Produto"].str.contains(nome, case=False, na=False)]

def buscar_por_periodo(periodo):
    return tabela[tabela["Período"].str.contains(periodo, case=False, na=False)]

def buscar_por_data(data):
    return tabela[tabela["Data"] == data]

def produtos_mais_vendidos(limite):
    if limite <= 0:
        return None
    else:
        return tabela.groupby("Produto")["Qtd"].sum().sort_values(ascending=False).head(limite) 
