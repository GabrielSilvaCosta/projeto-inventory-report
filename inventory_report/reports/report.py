from inventory_report.inventory import Inventory
from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def add_inventory(self, inventory: Inventory) -> None:
        pass

    @abstractmethod
    def generate(self) -> str:
        pass
