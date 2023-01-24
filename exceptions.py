class BaseError(Exception):
    message = "Неожиданная ошибка"


class RequestError(BaseError):
    message = "Ошибка обработки запроса"


class CourierError(BaseError):
    message = "Ошибка при доставке"


class NotEnoughSpace(CourierError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(CourierError):
    message = "Недостаточно товара на складе"


class TooManyDifferentProducts(CourierError):
    message = "Слишком много разных товаров"


class InvalidRequest(RequestError):
    message = "Неверный запрос. Попробуйте снова"


class InvalidStorageName(RequestError):
    message = "Выбран несуществующий склад"
