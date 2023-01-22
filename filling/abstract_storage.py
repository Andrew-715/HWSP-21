from abc import ABC, abstractmethod


class ABCStorage(ABC):
    @abstractmethod
    def add(self, name: str, quantity: int):
        pass

    @abstractmethod
    def remove(self, name: str, quantity: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
