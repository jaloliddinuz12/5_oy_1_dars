from telebot import TeleBot
from telebot.types import Message

# Bot tokeni
bot = TeleBot('8994079347:AAEPDQ1QmE2khoqbwjOiXRI6NTOlDUd-bWI')

@bot.message_handler(commands=["start"])
def reaction_start(message: Message):
    chat_id = message.chat.id
    print(f"Start bosgan foydalanuvchi IDsi: {chat_id}")
    bot.send_message(chat_id, "BOTDAN FOYDALANISH 1000$")

@bot.message_handler(commands=["help"])
def reaction_help(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "YORDAM BERISH 500$")

@bot.message_handler(commands=["support"])
def reaction_support(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Telegram manzilimiz: @jaloliddin_c1, PHONE CONTACT +998976627371")

@bot.message_handler(commands=["stop"])
def reaction_stop(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "BOTNI TOXTATISH 1000$")

@bot.message_handler(content_types=['text', 'video', 'photo', 'voice', 'sticker', 'document'])
def reaction_for_text(message: Message):
    chat_id = message.chat.id
    bot.copy_message(chat_id=chat_id, from_chat_id=chat_id, message_id=message.message_id)

bot.infinity_polling()