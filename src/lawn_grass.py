from src.product import Product


class LawnGrass(Product):
    """Класс для представления товара 'Lawn Grass' в интернет-магазине."""

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


if __name__ == "__main__":
    lawn_grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    print(lawn_grass.name)
    print(lawn_grass.description)
    print(lawn_grass.price)
    print(lawn_grass.quantity)
    print(lawn_grass.country)
    print(lawn_grass.germination_period)
    print(lawn_grass.color)
