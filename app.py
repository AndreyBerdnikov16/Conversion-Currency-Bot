import telebot
from config import keys, token
from extensions import APIException, ConverterCurrency
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Хэй! Чтобы начать работу, напиши команду в следующем формате: \n<валюта в которую хотите перевести>\
    <ваша валюта> \
    <количество вашей валюты>\nУвидеть список всех доступных валют: /values \nПолучить подсказку: /help"


    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = "Доступные валюты: "
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise ExchangeException('Введите команду или 3 параметра')

        quote, base, amount = values
        total_base = ConverterCurrency.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{amount} {base} = {total_base} {quote}'
        bot.send_message(message.chat.id, text)

bot.polling()