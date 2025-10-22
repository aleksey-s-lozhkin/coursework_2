import pytest

from src.category import Category
from src.product import Product


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
    return [
        Product("name1", "description1", 100.0, 5),
        Product("name2", "description2", 200.0, 3)
    ]


@pytest.fixture
def category_with_products(sample_products):
    return Category("name1", "description1", sample_products.copy())
