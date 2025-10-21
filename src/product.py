from typing import Any


class Product:
    """Класс для представления товара в интернет-магазине."""

    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict[str, Any]):
        result = cls(product['name'], product['description'], product['price'], product['quantity'])
        return result

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return

        self.__price = new_price
