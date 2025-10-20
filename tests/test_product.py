def test_product_init_first(first_product, second_product):
    """Тест на проверку корректности инициализации класса Product"""

    # Первый продукт
    assert first_product.name == 'name1'
    assert first_product.description == 'description1'
    assert first_product.price == 10.0
    assert first_product.quantity == 1

    #Второй продукт
    assert second_product.name == 'name2'
    assert second_product.description == 'description2'
    assert second_product.price == 20.0
    assert second_product.quantity == 2
