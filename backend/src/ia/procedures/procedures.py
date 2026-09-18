#Atenção esse é o arquivo que é para ser importado para utilizar as procedures
# ex:
#import procedures as proc

import vendas_procedures as vendas
import regras_procedures as regras
import produtos_procedures as produtos  
import ingredientes_procedures as ingredientes
import descarte_procedures as descarte

#como acessar?
# main.py ou telegram_bot.py ou tools/qualquer_arquivo_dspy.py
# import procedures

#Exemplos
# # Você acessa a função chamando o arquivo central > apelido do módulo > função 
# procedures.vendas.buscar_por_nome_produto()
# procedures.vendas.buscar_por_periodo()
# procedures.regras.buscar_por_dia()
# procedures.regras.buscar_por_semana_mes_ano() # (1, 9, 2026) -> traduzindo semana 1, do mes 9 do ano 2026
# procedures.descarte.buscar_por_produto()
# procedures.produto.buscar_por_setor()

