from typing import Any, Dict

import requests

from config.config import URL_API, TIMEOUT
from exceptions import ApiCallError, InvalidApiTokenError, InvalidParamsTypesError
from fields_validation import FieldsValidator


API_RESPONSE = Dict[str, Any]
API_TOKEN = str


class MarketCSGOAdapter:

    def __init__(self, api_token: API_TOKEN) -> None:
        FieldsValidator().validation_api_token(api_token)
        self.api_token: API_TOKEN = api_token

    @staticmethod
    def _api_call(url_path: str) -> API_RESPONSE:
        url = f"{URL_API}{url_path}"
        try:
            response = requests.get(url, timeout=TIMEOUT)
        except requests.RequestException:
            raise ApiCallError
        if response.status_code == 200:
            return response.json()
        raise ApiCallError

    def get_money(self) -> API_RESPONSE:
        return self._api_call(f"get_money?key={self.api_token}")

    def go_offline(self) -> API_RESPONSE:
        return self._api_call(f"go-offline?key={self.api_token}")

    def update_inventory(self) -> API_RESPONSE:
        return self._api_call(f"update-inventory?key={self.api_token}")

    def transfer_discounts(self, his_secret_key: API_TOKEN) -> API_RESPONSE:
        FieldsValidator().valadation_his_secret_key(his_secret_key)
        return self._api_call(f"transfer-discounts?key={self.api_token}&to={his_secret_key}")

    def set_add_to_sale(self, item_id: str, price: int, currency: str) -> API_RESPONSE:
        FieldsValidator().validation_item_id(item_id)
        FieldsValidator().validation_price(price)
        FieldsValidator().validation_currency(currency)
        return self._api_call(f"add-to-sale?key={self.api_token}&item_id={item_id}&price={price}&cur={currency}")

    def set_price(self, item_id: str, price: int, currency: str) -> API_RESPONSE:
        FieldsValidator().validation_item_id(item_id)
        FieldsValidator().validation_price(price)
        FieldsValidator().validation_currency(currency)
        return self._api_call(f"set-price?key={self.api_token}&item_id={item_id}&price={price}&cur={currency}")

    def remove_all_from_sale(self) -> API_RESPONSE:
        return self._api_call(f"remove-all-from-sale?key={self.api_token}")

    def ping(self) -> API_RESPONSE:
        return self._api_call(f"ping?key={self.api_token}")

    def item(self) -> API_RESPONSE:
        return self._api_call(f"item?key={self.api_token}")

    def trades(self) -> API_RESPONSE:
        return self._api_call(f"trades?key={self.api_token}")

    # рассмотерть медод trades на предмет extendeds , я предпологаю что это словарь \ так же меня смутил второй запрос \ единственная мысль сейчас это создать второй метод
    #     def trades_extendeds(self,extendeds_number) -> API_RESPONSE:
    #         return self._api_call(f"trades?key={self.api_token}&extended={extendeds_number}")\\ аргументируя тем что вариант имеет место быть в документации extended
    # выглядит как парметр но в запросе им не является \я предполагаю что меняется только номер

    def buy(self, item_id: str, price: int) -> API_RESPONSE:
        FieldsValidator().validation_item_id(item_id)
        FieldsValidator().validation_price(price)
        return self._api_call(f"buy?key={self.api_token}&item_id={item_id}&price={price}")

    def buy_market_hash_name(self, market_hash_name: str, price: int) -> API_RESPONSE:
        FieldsValidator().validation_market_hash_name(market_hash_name)
        FieldsValidator().validation_price(price)
        return self._api_call(f"buy?key={self.api_token}&market-hash-name={market_hash_name}&price={price}")

    ## метод  buy-for требует обсуждения \ указанные там параметры не совсем понятны
    # если я правильно понял то partner = his secret key , а token = его уникльному коду
    # если я прав то метод будет выглядить на примере метода с market_hash_name
    #    def buy_for_market_hash_name(self, market_hash_name: str, price: int, partner: API_TOKEN, token:str) -> API_RESPONSE:
    #    FieldsValidator().validation_market_hash_name(market_hash_name)
    #    FieldsValidator().validation_price(price)
    #    методы валидации не создавал \ так как ваириант спроный
    #    return self._api_call(f"buy-for?key={self.api_token}&market-hash-name={market_hash_name}&price={price}&partner=[partner]&token=[token]") get_buy_info_by_custom_id

    def get_buy_info_by_custom_id(self, custom_id: str) -> API_RESPONSE:
        FieldsValidator().validation_custom_id(custom_id)
        return self._api_call(f"get-buy-info-by-custom-id?key={self.api_token}&custom_id={custom_id}")

    def history(self, data: str) -> API_RESPONSE:
        return self._api_call(f"history?key={self.api_token}&date={data}")
# создать валидацию для даты

    def go_offline(self) -> API_RESPONSE:
        return self._api_call(f"go-offline?key={self.api_token}")

    def get_my_steam_id(self) -> API_RESPONSE:
        return self._api_call(f"get_my_steam_id?key={self.api_token}")

    def search_item_by_hash_name(self, market_hash_name: str) -> API_RESPONSE:
        FieldsValidator().validation_market_hash_name(market_hash_name)
        return self._api_call(f"search-item-by-hash-name?key={self.api_token}&hash_name={market_hash_name}")

    def search_item_by_hash_name_specific(self, market_hash_name: str) -> API_RESPONSE:
        FieldsValidator().validation_market_hash_name(market_hash_name)
        return self._api_call(f"search-item-by-hash-name-specific?key={self.api_token}&hash_name={market_hash_name}")

    def search_list_items_by_hash_name_all(self, market_hash_name: str) -> API_RESPONSE:
        FieldsValidator().validation_market_hash_name(market_hash_name)
        return self._api_call(f"search-list-items-by-hash-name-all?key={self.api_token}&hash_name={market_hash_name}")

    def get_list_items_info(self, market_hash_name: str) -> API_RESPONSE:
        FieldsValidator().validation_market_hash_name(market_hash_name)
        return self._api_call(f"get-list-items-info?key={self.api_token}&hash_name={market_hash_name}")

    def test(self) -> API_RESPONSE:
        return self._api_call(f"test?key={self.api_token}")

    def trade_request_take(self) -> API_RESPONSE:
        return self._api_call(f"trade-request-take?key={self.api_token}[&bot=botid]")

    def trade_request_give(self) -> API_RESPONSE:
        return self._api_call(f"trade-request-give?key={self.api_token}")

    def trade_request_give_p2p(self) -> API_RESPONSE:
        return self._api_call(f"trade-request-give-p2p?key={self.api_token}")

    def trade_request_give_p2p_all(self) -> API_RESPONSE:
        return self._api_call(f"trade-request-give-p2p-all?key={self.api_token}")

# прочитать что такое деккоратор \ ссылка есть в дискорте от жени \ прочитать про валидациюи прочитать как переместить валидацию в деккоратор