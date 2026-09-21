import telebot
from telebot.apihelper import ApiTelegramException
from ia.message import processar_mensagem

def iniciar_bot(bot_key):
    bot = telebot.TeleBot(bot_key)

    tipos_nao_suportados = [
        'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 
        'voice', 'location', 'contact', 'animation'
    ]
    
    @bot.message_handler(content_types=['text'])
    def receber_texto(message):
        print(f"[DEBUG] Mensagem recebida: {message.text}")

        msg_temp = bot.reply_to(message, "⏳ <b><i>Processando sua solicitação...</i></b>", parse_mode='HTML')
        bot.send_chat_action(message.chat.id, 'typing')

        resposta_bruta = str(processar_mensagem(message.text))
        resposta = resposta_bruta.replace('```html', '').replace('```', '').replace('[[ ## completed ]]', '').strip()

        print(f"[DEBUG] Resposta processada: {resposta}")
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg_temp.message_id,
            text=resposta
        )
    
    @bot.message_handler(content_types=tipos_nao_suportados)
    def receber_formatos_invalidos(message):
        bot.reply_to(
            message, 
            "Desculpe, no momento eu não suporto esse formato enviado. Por favor, me envie apenas mensagens de texto!"
        )

    print("Bot está online e ouvindo...")
    bot.infinity_polling()