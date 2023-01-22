from filling.courier import Courier
from filling.shop import Shop
from filling.store import Store
from filling.request import Request
from exceptions import RequestError, CourierError


store = Store(items={})
shop = Shop(items={})

store.items = {
    "холодильник": 14,
    "пылесос": 11,
    "утюг": 14,
    "стиральная машина": 8,
    "кондиционер": 13,
    "мультиварка": 7
}

shop.items = {
    "холодильник": 4,
    "пылесос": 1,
    "утюг": 2,
    "стиральная машина": 2,
    "кондиционер": 3
}

storages = {
    "магазин": shop,
    "склад": store
}

def main():
    while True:
        for storage_name  in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].items}')

        user_input = input(
            'Необходим запрос в формате "Доставить 1 утюг из склада в магазин"\n'
            'Введите "stop" или "стоп", если хотите закончить.'
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except CourierError as error:
            print(error.message)

if __name__ == '__main__':
    main()
