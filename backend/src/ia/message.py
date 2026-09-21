import dspy
from dspy.utils.exceptions import AdapterParseError
from ia.config import IA_APRIMORADA 
from ia.agentes import agente_filtro, agente_comunicador, agente_trabalhador

def processar_mensagem(texto_usuario: str) -> str:
    """Recebe a mensagem do Telegram e orquestra a resposta da IA."""
    
    # analise = agente_filtro(pergunta=texto_usuario)
    # resultado_filtro = str(analise.assunto_valido).strip().upper()
    # if "NAO" in resultado_filtro or "NÃO" in resultado_filtro:
    #     return "Desculpe, meu sistema é restrito à análise de supermercado."
        
    try:
        with dspy.context(lm=IA_APRIMORADA):
            resultado = agente_trabalhador(pergunta=texto_usuario)
            dspy.inspect_history(n=1)
            
            texto_final = agente_comunicador(
                pergunta_original=texto_usuario, 
                dado_bruto=resultado.dado_bruto_da_ferramenta
            )
            
        return texto_final.resposta_final

    except AdapterParseError as erro_dspy:
        print(f"[ERRO DSPY] O modelo travou e retornou nulo. Log: {erro_dspy}")
        return "⚠️ Ops! Minha inteligência artificial teve um branco e não conseguiu processar as ferramentas."
        
    except Exception as erro_geral:
        print(f"[ERRO GERAL IA] {erro_geral}")
        return "⚠️ Ocorreu um erro inesperado de conexão com a IA."