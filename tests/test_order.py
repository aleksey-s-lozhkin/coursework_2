import pytest

from src.exceptions import ZerroQuantity
from src.order import Order


def test_order_str(order_with_products):
    assert str(order_with_products) == 'Заказ: name1, количество: 5, итого: 1000.0 руб.'
