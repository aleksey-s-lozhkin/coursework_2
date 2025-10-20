import pytest
import json
import os
from unittest.mock import mock_open, patch

from src.category import Category
from src.product import Product
from src.utils import read_json, create_objects_from_json


def test_read_json_valid_file():
    """Тест чтения корректного JSON файла с использованием мока"""
    test_data = [{"name": "test", "value": 123}]
    mock_file = mock_open(read_data=json.dumps(test_data))

    with patch('builtins.open', mock_file):
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = test_data
            result = read_json('fake_path.json')

    assert result == test_data
    mock_file.assert_called_once_with(os.path.abspath('fake_path.json'), 'r', encoding='UTF-8')
    mock_json_load.assert_called_once_with(mock_file())


def test_read_json_file_not_found():
    """Тест обработки отсутствующего файла"""
    with pytest.raises(FileNotFoundError):
        read_json("nonexistent_file.json")


def test_create_objects():
    """Базовый тест создания объектов"""
    test_data = [
        {
            "name": "Электроника",
            "description": "Техника",
            "products": [
                {
                    "name": "Телефон",
                    "description": "Смартфон",
                    "price": 10000.0,
                    "quantity": 5
                }
            ]
        }
    ]

    categories = create_objects_from_json(test_data)

    # Проверяем структуру
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert isinstance(categories[0].products[0], Product)

    # Проверяем атрибуты
    assert categories[0].name == "Электроника"
    assert categories[0].products[0].name == "Телефон"
    assert categories[0].products[0].price == 10000.0
