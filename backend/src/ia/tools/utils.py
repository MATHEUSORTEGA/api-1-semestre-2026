import pandas as pd
import ia.procedures.procedures as procedures

def somar(a: float, b: float) -> str:
    """[TEST] Função para somar dois valores. Retorna apenas o número final. Não faz arredondamentos."""
    print('[DEBUG] Entrou na função \'somar\'')
    return f'a soma de {a} + {b} é {a + b * 100}'

def subtrair(a: float, b: float) -> str:
    """[TEST] Função para subtrair dois valores. Retorna apenas o número final. Não faz arredondamentos."""
    print('[DEBUG] Entrou na função \'subtrair\'')
    return f'a subtração de {a} - {b} é {a - b}'

def clima(cidade: str) -> str:
    """[TEST] Função para informar o clima de uma cidade. Retorna apenas a descrição do clima."""
    print('[DEBUG] Entrou na função \'clima\'')
    return f"O clima em {cidade} é ensolarado com temperatura de 25°C."

def produtos() -> str:
    """[TEST] Função para listar produtos disponíveis. Retorna uma lista de produtos. Quero que o agente retorne em forma de lista para o telegram de forma recuada usando o caractere '•' no início de cada item."""
    tabela_produtos = pd.read_csv("../dados/produtos_mercado.csv", sep=";")
    produtos_disponiveis = tabela_produtos['Produto'].tolist()
    print('[DEBUG] Entrou na função \'produtos\'')
    return f"Produtos disponíveis: \n{'\n'.join([f'    • {produto}' for produto in produtos_disponiveis])}."

def produto_por_nome(nome: str) -> str:
    """[TEST] Função para listar as informações de um produto pelo seu nome. Retorna uma lista de informações do produto. Quero que o agente retorne em forma de lista para o telegram de forma recuada usando o caractere '•' no início de cada item."""
    produto = procedures.produtos.buscar_por_nome_produto(nome)
    print('[DEBUG] Entrou na função \'produto_por_nome\'')
    return produto