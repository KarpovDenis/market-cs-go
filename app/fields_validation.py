from typing import Any, Dict

from exceptions import ApiCallError, InvalidApiTokenError, InvalidParamsTypesError, InvalidParamsError



CURRENCY = {"RUB", "USD", "EUR"}
API_TOKEN = str

class FieldsValidator:

    @staticmethod
    def validation_price(price):
        if not isinstance(price, int):
            raise InvalidParamsTypesError

    @staticmethod
    def validation_item_id(item_id):
        if not isinstance(item_id, str):
            raise InvalidParamsTypesError

    @staticmethod
    def validation_custom_id(custom_id):
        if not isinstance(custom_id, str):
            raise InvalidParamsTypesError

    @staticmethod
    def validation_currency(currency):
        if not isinstance(currency, str):
            raise InvalidParamsTypesError
        if currency in CURRENCY:
            raise InvalidParamsError

    @staticmethod
    def valadation_his_secret_key(his_secret_key):
        if not isinstance(his_secret_key, API_TOKEN):
            raise InvalidApiTokenError

    @staticmethod
    def validation_api_token(api_token):
        if not isinstance(api_token, API_TOKEN):
            raise InvalidApiTokenError

    @staticmethod
    def validation_market_hash_name(market_hash_name):
        if not isinstance(market_hash_name, str):
            raise InvalidParamsTypesError






