from typing import Any, List

from src.base_product import BaseProduct
from src.consol_mixin import ConsolMixin


class Product(BaseProduct, ConsolMixin):
    """Класс для представления товара в интернет-магазине."""

    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product: dict[str, Any], products: List['Product'] | None) -> 'Product':
        """Метод создает новый товар"""

        if products is None:
            products = []

        for item in products:
            if item.name == product['name']:
                item.quantity += product['quantity']
                if product['price'] > item.price:
                    item.price = product['price']
                return item

        return cls(product['name'], product['description'], product['price'], product['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return

        if new_price < self.__price:
            if input('Новая цена меньше прошлой. Введите "y" - для подтверждения: ') != 'y':
                return

        self.__price = new_price


if __name__ == '__main__':
    product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
