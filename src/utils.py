import json
import os
from typing import Any, List

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Функция для чтения json файла"""

    fullpath = os.path.abspath(path)
    with open(fullpath, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: List[dict]) -> list:
    """Функция для создания объектов из json файла"""

    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    raw_data = read_json('../data/products.json')
    categories_data = create_objects_from_json(raw_data)
    print(categories_data)

    print(categories_data[0].name)
    print(categories_data[0].products)
