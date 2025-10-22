def test_category_init(first_category, second_category):
    """Тест на проверку корректности инициализации класса Category"""

    assert first_category.name == 'name1'
    assert first_category.description == 'description1'
    assert len(first_category.products_in_list) == 2
    assert first_category.category_count == 2
    assert first_category.product_count == 4

    assert second_category.name == 'name2'
    assert second_category.description == 'description2'
    assert len(second_category.products_in_list) == 2


def test_category_products_property(category_with_products, sample_products):
    """Проверка корректности форматирования строки с товарами"""

    products_str = category_with_products.products
    expected_lines = [
        f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        for product in sample_products
    ]
    expected = "\n".join(expected_lines) + "\n"
    assert products_str == expected
