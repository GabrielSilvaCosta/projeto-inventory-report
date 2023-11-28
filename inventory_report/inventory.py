from inventory_report.product import Product
from typing import Optional


class Inventory:
    def __init__(self, data: Optional[list[Product]] = None) -> None:
        self.__data: list[Product] = data if data is not None else []

    def add_data(self, data: list[Product]) -> None:
        self.__data += data

    @property
    def data(self) -> list[Product]:
        return self.__data.copy()
