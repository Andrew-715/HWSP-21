from filling.base_storage import BaseStorage


class Store(BaseStorage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)
