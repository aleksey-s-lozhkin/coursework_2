from src.base_category import BaseCategory
from src.exceptions import ZerroQuantity
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
            try:
                if product.quantity == 0:
                    raise ZerroQuantity('Нельзя добавить продукт с нулевым количеством товара')
            except ZerroQuantity as err:
                print(str(err))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print('Товар успешно добавлен')
            finally:
                print('Обработка добавления товара завершена')
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        """Метод, который подсчитывает средний ценник всех товаров"""

        try:
            return round(sum([item.price for item in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category2 = Category("Смартфоны", "Категория смартфонов", [])

    print(category2.middle_price())
