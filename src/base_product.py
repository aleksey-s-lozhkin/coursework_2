from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Создание базового абстрактного класса для класса Product"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
