from abc import ABC, abstractmethod


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if len(value.strip()) != 3 or ' ' in value.strip():
            raise ValueError("Store location must be 3 chars long!")
        self._location = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self._capacity = value

    @property
    @abstractmethod
    def store_type(self):
        pass

    @abstractmethod
    def store_stats(self):
        pass

    def get_estimated_profit(self):
        profit = 0.1
        total_price = sum(product.price for product in self.products)
        profit = total_price * profit
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

