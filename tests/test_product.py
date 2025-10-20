def test_product_init_first(first_product):
    assert first_product.name == 'name1'
    assert first_product.description == 'description1'
    assert first_product.price == 10.0
    assert first_product.quantity == 1


def test_product_init_second(second_product):
    assert second_product.name == 'name2'
    assert second_product.description == 'description2'
    assert second_product.price == 20.0
    assert second_product.quantity == 2
