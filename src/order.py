from src.base_category import BaseCategory
from src.exceptions import ZerroQuantity
from src.product import Product


class Order(BaseCategory):
    """Клас для предоставления заказа в интернет магазине"""

    def __init__(self, product: Product, quantity: int):

        try:
            if quantity == 0:
                raise ZerroQuantity('Нельзя создать заказ с нулевым количеством товара')
        except ZerroQuantity as err:
            print(str(err))
        else:
            print('Товар успешно добавлен в заказ')
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity
        finally:
            print('Обработка добавления товара завершена')

    def __str__(self):

        return f'Заказ: {self.product.name}, количество: {self.quantity}, итого: {self.total_price} руб.'

    @property
    def total_products(self) -> int:

        return self.quantity

    @property
    def products_list(self) -> str:

        return f'{self.product.name} - {self.quantity} шт.'


if __name__ == '__main__':
    product = Product("name", "description", 200.0, 5)
    order = Order(product, 0)

    product1 = Product("name", "description", 200.0, 5)
    order1 = Order(product1, 2)
