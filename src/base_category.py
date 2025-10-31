from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """Абстрактный базовый клас для класса Category"""

    @property
    @abstractmethod
    def total_products(self) -> int:
        pass

    @property
    @abstractmethod
    def products_list(self) -> str:
        pass
