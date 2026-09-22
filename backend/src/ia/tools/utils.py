TOOLS_DISPONIVEIS = []

def dspy_tool(func):
    """Decorador: adiciona a função à lista de ferramentas do DSPy."""
    TOOLS_DISPONIVEIS.append(func)
    return func

# --- REGISTRO DE ARQUIVOS DE FERRAMENTAS ---
# O Python precisa ler esses arquivos uma única vez para ativar os decoradores.
# Sempre que criar um arquivo novo (ex: vendas.py), adicione um import genérico aqui:

import ia.tools.produtos_tools
import ia.tools.vendas
import ia.tools.descartes
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
def classificar_dia(data: str) -> int:
    """
    Classifica se o dia é bom (1) ou ruim (0).
    Condições para dia bom: dia de pagamento, sexta a domingo, ou feriado.
    """
    # 1. Verifica se é dia de pagamento (usa a função já existente)
    # Se a distância for 0, significa que é o próprio dia do pagamento
    if dias_ate_pagamento(data) == 0:
        return 1
        
    # Converte a string para objeto datetime para extrair o dia da semana e o dia/mês
    dt = datetime.strptime(data, "%d/%m/%Y")
    
    # 2. Verifica se é sexta (4), sábado (5) ou domingo (6)
    if dt.weekday() in [4, 5, 6]:
        return 1
        
    # 3. Verifica se é feriado (lista de feriados fixos nacionais como exemplo)
    feriados_fixos = [
        "01/01",  # Ano Novo
        "21/04",  # Tiradentes
        "01/05",  # Dia do Trabalho
        "07/09",  # Independência do Brasil
        "12/10",  # Nossa Sra. Aparecida
        "02/11",  # Finados
        "15/11",  # Proclamação da República
        "25/12"   # Natal
    ]
    
    # Extrai apenas o dia e o mês da data inserida para comparar com a lista
    dia_mes = dt.strftime("%d/%m")
    if dia_mes in feriados_fixos:
        return 1
        
    # Se nenhuma das condições acima for satisfeita, o dia é ruim
    return 0

# --- TESTES DO DIA BOM OU RUIM ---
if __name__ == "__main__":
    # Teste 1: Dia de pagamento isolado (07/10/2026 é o 5º dia útil, uma quarta-feira)
    print("Dia é de pagamento, deve retornar 1; Resultado:", classificar_dia("07/10/2026"))
    
    # Teste 2: Feriado isolado (07/09/2026 é feriado, uma segunda-feira)
    print("Dia é feriado, deve retornar 1; Resultado:", classificar_dia("07/09/2026"))
    
    # Teste 3: Fim de semana isolado (20/09/2026 é um domingo)
    print("Dia é sexta, sábado ou domingo, deve retornar 1; Resultado:", classificar_dia("20/09/2026"))
    
    # Teste 4: Dia mau (21/09/2026 é uma segunda-feira normal)
    print("Dia é um dia da semana (segunda, terça, quarta ou quinta), sem ser feriado ou dia de pagamento. Resultado:", classificar_dia("21/09/2026"))