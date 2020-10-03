import telebot
from telebot import types
from telebot.types import Message
import Selenium_IWP
from selenium.common.exceptions import NoSuchElementException
from Soup_IWP import Parser

TOKEN = '1192040115:AAGI36vt-M7k7SWhMNt3OjmeI06Lmfl4cGE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def commands(message: Message):
    if message.text == '/start':
        bot.send_message(message.chat.id, '👾 Введите название игры:')
        bot.register_next_step_handler(message, Sel_IWP)
    elif message.text == '/help':
        bot.send_message(message.chat.id,
                         '🎮 Я бот, который поможет тебе найти игру по самой дешевой цене из проверенных источников \n'
                         'Просто напиши мне /start и следуй моим указаниям\n\n'
                         'Мне часто приходится искать ключи для игр с вкусной ценой, поэтому был написан этот простой бот. Надеюсь, он тебе будет полезен\n'
                         '🎮 Для связи: @Pol1naQ / @Shubinat ')

@bot.message_handler(content_types=['text'])
def Sel_IWP(message: Message):
    if message.text != '/help':
        name_game = message.text
        bot.send_message(message.chat.id, '🎮 Идет поиск игр...')
        all_games, driver = Selenium_IWP.find_game(name_game)
        if any(all_games):
            games_result = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            for game in list(all_games.keys()):
                games_result.add(game)
            bot.send_message(message.chat.id, 'Выбери игру из списка: ', reply_markup=games_result)
            bot.register_next_step_handler(message, GetPrices, driver, all_games)
        else:
            bot.send_message(message.chat.id, 'Я не смог ничего найти по твоему запросу. Ты точно ввел все правильно? А может игра бесплатная?\n'
                                              '🎮 Если ты уверен, что ввел все правильно, то, видимо, такой игры нет в нашей базе. Но мы работаем над этим!')
    else:
        bot.send_message(message.chat.id,
                         '🎮 Я бот, который поможет тебе найти игру по самой дешевой цене из проверенных источников \n'
                         'Просто напиши мне /start и следуй моим указаниям\n\n'
                         'Мне часто приходится искать ключи для игр с вкусной ценой, поэтому был написан этот простой бот. Надеюсь, он тебе будет полезен\n'
                         '🎮 Для связи: @Pol1naQ / @Shubinat ')
@bot.message_handler(content_types=['text'])
def GetPrices (message: Message, driver, all_games):
    if message.text != '/help' and message.text != 'start':
        url = Selenium_IWP.get_url(all_games[message.text], driver)
        bot.send_message(message.chat.id, Parser(url, message.text))
    elif message.text == '/start':
        bot.send_message(message.chat.id, '👾 Введите название игры:')
        bot.register_next_step_handler(message, Sel_IWP)
    else:
        bot.send_message(message.chat.id,
                         '🎮 Я бот, который поможет тебе найти игру по самой дешевой цене из проверенных источников \n'
                         'Просто напиши мне /start и следуй моим указаниям\n\n'
                         'Мне часто приходится искать ключи для игр с вкусной ценой, поэтому был написан этот простой бот. Надеюсь, он тебе будет полезен\n'
                         '🎮 Для связи: @Pol1naQ / @Shubinat ')

bot.polling(timeout=60)
