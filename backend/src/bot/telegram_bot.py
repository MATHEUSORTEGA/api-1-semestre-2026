import telebot
from ia.config import processar_mensagem

def iniciar_bot(bot_key):
    bot = telebot.TeleBot(bot_key)

    tipos_nao_suportados = [
        'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 
        'voice', 'location', 'contact', 'animation'
    ]
    
    @bot.message_handler(content_types=['text'])
    def receber_texto(message):
        resposta = processar_mensagem(message.text)
        bot.reply_to(message, str(resposta))
    
    @bot.message_handler(content_types=tipos_nao_suportados)
    def receber_formatos_invalidos(message):
        bot.reply_to(
            message, 
            "Desculpe, no momento eu não suporto esse formato enviado. Por favor, me envie apenas mensagens de texto!"
        )

    print("Bot está online e ouvindo...")
    bot.infinity_polling()