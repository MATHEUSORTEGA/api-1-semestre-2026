TOOLS_DISPONIVEIS = []

def dspy_tool(func):
    """Decorador: adiciona a função à lista de ferramentas do DSPy."""
    TOOLS_DISPONIVEIS.append(func)
    return func


# --- REGISTRO DE ARQUIVOS DE FERRAMENTAS ---
# O Python precisa ler esses arquivos uma única vez para ativar os decoradores.
# Sempre que criar um arquivo novo (ex: vendas.py), adicione um import genérico aqui:

#import ia.tools.produtos_tools
# import ia.tools.vendas
# import ia.tools.descartes

from datetime import datetime, timedelta

def dias_ate_pagamento(valor: str) -> int:
    data_alvo = datetime.strptime(valor, "%d/%m/%Y")
    
    def sim_pagamento(d):
        # 1. Regra do dia 20 (antecipa se for fim de semana)
        dia_20 = d.replace(day=20)
        if dia_20.weekday() == 5: dia_20 = dia_20.replace(day=19) # Sábado
        if dia_20.weekday() == 6: dia_20 = dia_20.replace(day=18) # Domingo
        if d.date() == dia_20.date(): 
            return True
            
        # 2. Regra do 5º dia útil
        dias_uteis = 0
        for i in range(1, 32):
            try:
                data_teste = d.replace(day=i)
                if data_teste.weekday() <= 4: # 0 a 4 = Segunda a Sexta
                    dias_uteis += 1
                if dias_uteis == 5:
                    return d.date() == data_teste.date()
            except ValueError:
                break # Sai do loop se o dia não existir no mês (ex: 31 de fev)
        
        return False

    # Expande a busca dia a dia a partir da data alvo
    for i in range(20):
        if sim_pagamento(data_alvo + timedelta(days=i)):
            return -i # Futuro (negativo)
        if sim_pagamento(data_alvo - timedelta(days=i)):
            return i  # Passado (positivo)

print(dias_ate_pagamento("20/09/2026"))