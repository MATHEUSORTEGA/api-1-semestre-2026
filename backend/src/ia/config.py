import dspy
from ia.tools.utils import somar, subtrair, clima, produtos, produto_por_nome

IA_FILTRO = dspy.LM(model="ollama/gemma3:1b", api_base="http://localhost:11434")
IA_APRIMORADA = dspy.LM(model="ollama/gemma4:e2b", api_base="http://localhost:11434")

dspy.configure(lm=IA_FILTRO)

# 1. Filtro inicial
class FiltroDeIntencao(dspy.Signature):
    """Você é um classificador lógico de um sistema de supermercado.
    Sua ÚNICA função é identificar se o assunto faz parte do seu escopo de trabalho.
    Escopos válidos: produção, estoque, planilhas, lucros, desperdício e cálculos matemáticos.
    """
    pergunta = dspy.InputField(desc="Mensagem do usuário.")
    assunto_valido = dspy.OutputField(desc="Responda ESTRITAMENTE com a palavra 'SIM' ou com a palavra 'NAO'. Não escreva mais nada.")

class FormatadorDeResposta(dspy.Signature):
    """Você é um assistente virtual focado na análise de produção do supermercado.
    
    REGRAS ABSOLUTAS:
    1. Responda SEMPRE em Português do Brasil.
    2. Responda APENAS com base no Dado Bruto fornecido.
    3. Se o Dado Bruto contiver uma lista (ex: itens com '•' ou quebras de linha), MANTENHA A LISTA INTACTA na sua resposta, linha por linha. Nunca junte itens de uma lista no mesmo parágrafo.
    4. Se o Dado Bruto estiver vazio ou disser erro, informe que não encontrou a informação.
    5. Seja claro e amigável.
    """
    pergunta_original = dspy.InputField()
    dado_bruto = dspy.InputField(desc="Resultado numérico ou extração da ferramenta. Se for uma lista, ela possui quebras de linha '\\n' que devem ser mantidas.")
    resposta_final = dspy.OutputField(desc="A resposta final, mantendo a formatação de lista do Dado Bruto intacta.")

# 2. Agentes
agente_filtro = dspy.Predict(FiltroDeIntencao)
agente_comunicador = dspy.Predict(FormatadorDeResposta)
agente_trabalhador = dspy.ReAct("pergunta: str -> dado_bruto_da_ferramenta: str", tools=[somar, subtrair, clima, produtos, produto_por_nome])

def processar_mensagem(texto_usuario):
    # analise = agente_filtro(pergunta=texto_usuario)
    # resultado_filtro = str(analise.assunto_valido).strip().upper()
    
    # if "NAO" in resultado_filtro or "NÃO" in resultado_filtro or "NO" in resultado_filtro:
    #   return "Desculpe, meu sistema é restrito à análise de produção e estoque do supermercado. Não posso te ajudar com essa solicitação."
        
    with dspy.context(lm=IA_APRIMORADA):
        resultado = agente_trabalhador(pergunta=texto_usuario)
        dspy.inspect_history(n=1)
        
        texto_final = agente_comunicador(
            pergunta_original=texto_usuario, 
            dado_bruto=resultado.dado_bruto_da_ferramenta
        )
        
    return texto_final.resposta_final