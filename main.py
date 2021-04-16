import json
import requests
import telebot
from utils import ConversionException, CryptoConverter
TOKEN = '1692065554:AAFf5MRfTKg2EL5PUoBS50J8eVN1BEYsMmU'
bot = telebot.TeleBot(TOKEN)
keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
}
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nувидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message) -> object:
    values = message.text.split(' ')

    quote, base, amount = mesage.text.split(' ')
    quote, base, amount != values
    quote_ticker, base_ticker = keys[quote], keys[base]
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()