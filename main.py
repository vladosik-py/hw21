from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import RequestError, CourierError


store = Store(items={})
shop = Shop(items={})

store.items = {
    "печенька": 25,
    "собачка": 25,
    "ёлка": 25,
    "пончик": 3,
    "зонт": 5,
    "ноутбук": 1,
}

shop.items = {
    "печенька": 2,
    "собачка": 2,
    "ёлка": 2,
    "пончик": 1,
    "зонт": 1,
}

storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    print('\nДобрый день!\n')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].items}')

        user_input = input(
            'Введите запрос в формате "Доставить 3 печенька из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storages=storages,
        )

        try:
            courier.move()
        except CourierError as error:
            print(error.message)


if __name__ == '__main__':
    main()
