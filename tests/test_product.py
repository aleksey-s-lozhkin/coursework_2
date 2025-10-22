from src.product import Product


def test_product_init_first(first_product, second_product):
    """Тест на проверку корректности инициализации класса Product"""

    # Первый продукт
    assert first_product.name == 'name1'
    assert first_product.description == 'description1'
    assert first_product.price == 10.0
    assert first_product.quantity == 1

    # Второй продукт
    assert second_product.name == 'name2'
    assert second_product.description == 'description2'
    assert second_product.price == 20.0
    assert second_product.quantity == 2


def test_product_price_getter(first_product):
    assert first_product.price == 10.0


def test_product_price_setter_valid(first_product):
    first_product.price = 15.0
    assert first_product.price == 15.0


def test_product_price_setter_negative(first_product, capsys):
    first_product.price = -5.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert first_product.price == 10.0


def test_new_product_creation(sample_products):
    """Тест создания нового продукта, которого нет в списке"""

    product_data = {"name": "new_product", "description": "new_description", "price": 100.0, "quantity": 10}
    new_product = Product.new_product(product_data, [])
    assert new_product.name == "new_product"
    assert new_product.description == "new_description"
    assert new_product.price == 100.0
    assert new_product.quantity == 10


def test_new_product_update_existing(first_product):
    """Тест обновления существующего продукта"""

    product_data = {"name": first_product.name, "description": "updated_description", "price": 15.0, "quantity": 5}
    updated_product = Product.new_product(product_data, [first_product])
    assert updated_product is first_product
    assert updated_product.quantity == 6
    assert updated_product.price == 15.0


def test_new_product_update_existing_lower_price(first_product):
    """Тест обновления существующего продукта с более низкой ценой"""
    product_data = {
        "name": first_product.name,
        "description": "updated_description",
        "price": 8.0,  # ниже текущей 10.0
        "quantity": 5,
    }
    updated_product = Product.new_product(product_data, [first_product])
    assert updated_product is first_product
    assert updated_product.quantity == 6
    assert updated_product.price == 10.0
