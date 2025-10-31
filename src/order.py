from src.base_category import BaseCategory
from src.product import Product


class Order(BaseCategory):
    """Клас для предоставления заказа в интернет магазине"""

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        return f'Заказ: {self.product.name}, количество: {self.quantity}, итого: {self.total_price} руб.'

    @property
    def total_products(self) -> int:
        return self.quantity

    @property
    def products_list(self) -> str:
        return f'{self.product.name} - {self.quantity} шт.'
