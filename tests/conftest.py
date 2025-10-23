import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_product():
    return Product('name1', 'description1', 10.0, 1)


@pytest.fixture
def second_product():
    return Product('name2', 'description2', 20.0, 2)


@pytest.fixture
def first_category():
    return Category('name1', 'description1', ['prod1', 'prod2'])


@pytest.fixture
def second_category():
    return Category('name2', 'description2', ['prod3', 'prod4'])


@pytest.fixture
def sample_products():
    return [Product("name1", "description1", 100.0, 5), Product("name2", "description2", 200.0, 3)]


@pytest.fixture
def category_with_products(sample_products):
    return Category("name1", "description1", sample_products.copy())


@pytest.fixture
def category_with_three_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def product_iterator(category_with_three_products):
    return ProductIterator(category_with_three_products)
