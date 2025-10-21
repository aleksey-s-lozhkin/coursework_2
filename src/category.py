from src.product import Product


class Category:
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

    @property
    def products(self):
        product_str = ''
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1
