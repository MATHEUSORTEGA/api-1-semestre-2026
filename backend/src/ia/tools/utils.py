TOOLS_DISPONIVEIS = []

def dspy_tool(func):
    """Decorador: adiciona a função à lista de ferramentas do DSPy."""
    TOOLS_DISPONIVEIS.append(func)
    return func


# --- REGISTRO DE ARQUIVOS DE FERRAMENTAS ---
# O Python precisa ler esses arquivos uma única vez para ativar os decoradores.
# Sempre que criar um arquivo novo (ex: vendas.py), adicione um import genérico aqui:

import ia.tools.produtos
# import ia.tools.vendas
# import ia.tools.descartes