from typing import Dict

from abstract_storage import ABCStorage
from exceptions import NotEnoughSpace, NotEnoughProduct


class BaseStorage(ABCStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, quantity: int):
        if self.get_free_space() < quantity:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += quantity
        else:
            self.__items[name] = quantity

    def remove(self, name: str, quantity: int):
        if name not in self.__items or self.__items[name] < quantity:
            raise NotEnoughProduct

        self.__items[name] -= quantity
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        total_quantity = sum(self.__items.values())
        free_space = self.__capacity - total_quantity
        return free_space

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, new_data):
        self.__items = new_data

    def get_unique_items_count(self):
        return len(self.__items)
