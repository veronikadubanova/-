import requests
import json

class ConversionException(Exception):
    pass

class CryptoConverter:
    pass
    def convert(quote: str, base: str, amount: str):

        if len(values) > 3:
            raise ConversionException('Слишком много параметров')

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}')



