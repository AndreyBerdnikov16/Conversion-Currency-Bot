import requests
import json
from config import keys


class APIException(Exception):
    pass


class ConverterCurrency:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {quote}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {ифыу}")

        try:
            amount = int(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество валюты {amount}')

        if amount <= 0:
            raise APIException(f'Невозможно конвертировать количество валюты меньше 0')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = float(json.loads(r.content)[keys[quote]]) * amount
        return total_base