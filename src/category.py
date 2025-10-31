from src.base_category import BaseCategory
from src.product import Product


class Category(BaseCategory):
    """Класс для представления категории товаров в интернет-магазине."""

    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.total_products} шт.'

    @property
    def products_list(self) -> str:
        product_str = ''
        for product in self.__products:
            product_str += f'{str(product)}\n'
        return product_str

    @property
    def total_products(self) -> int:
        return sum(product.quantity for product in self.__products)

    def add_product(self, product: Product) -> None:
        """Метод добавляет товар в категорию"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products
