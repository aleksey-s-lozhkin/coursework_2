import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.order import Order
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def order_with_products():
    # Создаем один продукт, а не список
    product = Product("name1", "description1", 200.0, 5)
    return Order(product, 5)
