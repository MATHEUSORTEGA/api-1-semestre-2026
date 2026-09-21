import dspy
from ia.tools.utils import TOOLS_DISPONIVEIS

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
    3. Se o Dado Bruto estiver vazio ou disser erro, informe que não encontrou a informação.
    4. Seja claro e amigável.
    5. OBRIGATÓRIO: Para criar listas, use EXCLUSIVAMENTE o caractere especial '-' (hífen). É ESTRITAMENTE PROIBIDO usar asteriscos (*) no início das linhas.
    """
    pergunta_original = dspy.InputField()
    dado_bruto = dspy.InputField(desc="Resultado numérico ou extração da ferramenta. Mantenha quebras de linha '\\n'.")
    resposta_final = dspy.OutputField(desc="A resposta final estruturada e preenchida estritamente com base no dado bruto.")

agente_filtro = dspy.Predict(FiltroDeIntencao)
agente_comunicador = dspy.Predict(FormatadorDeResposta)

agente_trabalhador = dspy.ReAct(
    "pergunta: str -> dado_bruto_da_ferramenta: str", 
    tools=TOOLS_DISPONIVEIS
)