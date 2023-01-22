from typing import Dict

from filling.abstract_storage import ABCStorage
from filling.request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, ABCStorage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(name=self.__request.product, quantity=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} '
              f'{self.__request.product} из {self.__request.departure}')

        self.__to.add(name=self.__request.product, quantity=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} '
              f'{self.__request.product} в {self.__request.destination}')
