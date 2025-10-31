import pytest


def test_lawn_grass_init(lawn_grass1):
    """Тест на проверку корректности инициализации класса LawnGrass"""

    assert lawn_grass1.name == 'Газонная трава'
    assert lawn_grass1.description == 'Элитная трава для газона'
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == 'Россия'
    assert lawn_grass1.germination_period == '7 дней'
    assert lawn_grass1.color == 'Зеленый'


def test_lawn_grass_add(lawn_grass1, lawn_grass2):
    """Тест проверки сложения двух продуктов"""

    assert lawn_grass1 + lawn_grass2 == 500.0 * 20 + 450.0 * 15


def test_lawn_grass_add_error(lawn_grass1):
    """Тест проверки на ошибку если слагаемое не относится к классу LawnGrass"""

    with pytest.raises(TypeError):
        result = lawn_grass1 + 1
