class ApiCallError(Exception):
    """Ошибка соединения с API сервером."""


class InvalidApiTokenError(Exception):
    """Передан некорректный API token."""


class InvalidParamsError(Exception):
    """Передан некорректный параметр запроса."""


class InvalidParamsTypesError(InvalidParamsError):
    """Передан некорректный тип параметра запроса."""



