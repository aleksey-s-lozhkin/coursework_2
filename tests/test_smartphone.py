import pytest


def test_smartphone_init(smartphone1):
    """Тест на проверку корректности инициализации класса Smartphone"""

    assert smartphone1.name == 'Iphone 15'
    assert smartphone1.description == '512GB, Gray space'
    assert smartphone1.price == 210000.0
    assert smartphone1.quantity == 8
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == '15'
    assert smartphone1.memory == 512
    assert smartphone1.color == 'Gray space'


def test_smartphone_add(smartphone1, smartphone2):
    """Тест проверки сложения двух продуктов"""

    assert smartphone1 + smartphone2 == 210000.0 * 8 + 31000.0 * 14


def test_smartphone_add_error(smartphone1):
    """Тест проверки на ошибку если слагаемое не относится к классу Smarphone"""

    with pytest.raises(TypeError):
        result = smartphone1 + 1
