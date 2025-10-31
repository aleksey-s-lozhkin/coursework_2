def test_order_str(order_with_products):
    assert str(order_with_products) == 'Заказ: name1, количество: 5, итого: 1000.0 руб.'
