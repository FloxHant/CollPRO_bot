import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для игры в покемонов, скорее попробуй создать себе покемона, нажимай - /go")

@bot.message_handler(commands=['attack'])
def start(message): 
    if message.reply_to_message:
        pokemon_my = Pokemon.pokemons[message.fron.user.username]
        pokemon_enemy = Pokemon.pokemons[essage.reply_to_message.from_user.username]
        result = pokemon_my.attack(pokemon.enemy)
        bot.send_message(message.chat.id, result)
    else:   
        bot.send_message(message.chat.id, "Нужно отправить /attack в ответ на сообщение")

@bot.message_handler(commands=['/info'])
def info_handler(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pok = Pokemon.pokemons[username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.send_message(message.chat.id, "У вас ещё нет покемона. Создайте его командой /go")

bot.infinity_polling(none_stop=True)


