from mailbox import Message

from telebot import TeleBot

bot = TeleBot('8994079347:AAEPDQ1QmE2khoqbwjOiXRI6NTOlDUd-bWI')

@bot.message_handler(commands=["start"])
def reation_for_massage(message: Message):
    chat_id = message.chat.id
    print(chat_id)
    bot.send_message(chat_id, "BOTDAN FOYDALANISH 1000$")

@bot.message_handler(commands=["help"])
def reation_for_massage(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "YORDAM BERISH 500$")

@bot.message_handler(commands=["support"])
def reation_for_massage(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, " Telegram manzilimiz; @jaloliddin_c1, PHONE CONTACT +998976627371 ")

@bot.message_handler(commands=["stop"])
def reation_for_massage(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "BOTNI TOXTATISH 1000$")

@bot.message_handler(content_types=['text', 'video', 'photo', 'gift', 'voice', 'sticker', 'document'],
                     chat_types=['private'])
def reaction_for_text(message: Message):
    from_chat_id = message.chat.id

    if from_chat_id == 7061766664:
         chat_ids = [
              -1003740389338
         ]
         for chat_id in chat_ids:
            bot.copy_message(chat_id, from_chat_id, message.message_id)
    else:
        bot.copy_message(chat_id, from_chat_id, message.message_id)

bot.infinity_polling()
