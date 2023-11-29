from datetime import datetime, date
from typing import List
import pytest
from inventory_report.inventory import Inventory
from inventory_report.reports import CompleteReport, Report
from tests.conftest import OLDEST_DATE


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing_date = self.get_oldest_date("manufacturing_date")
        closest_expiration_date = self.get_oldest_date("expiration_date", True)
        largest_inventory_company = self.get_largest_inventory_company()

        result = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_company}"
        )

        return result

    def get_oldest_date(
        self, attribute: str, filter_expired: bool = False
    ) -> str:
        today = date.today()
        valid_dates = [
            datetime.strptime(getattr(product, attribute), "%Y-%m-%d").date()
            for inventory in self.inventories
            for product in inventory.data
            if (
                not filter_expired
                or datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                ).date()
                > today
            )
        ]

        if not valid_dates:
            return "N/A"

        return min(valid_dates).strftime("%Y-%m-%d")

    def get_largest_inventory_company(self) -> str:
        company_inventory = {}
        for inventory in self.inventories:
            for product in inventory.data:
                company_inventory[product.company_name] = (
                    company_inventory.get(product.company_name, 0) + 1
                )

        return max(company_inventory, key=company_inventory.get, default="N/A")


@pytest.mark.dependency
def test_generate_returns_correct_oldest_date(
    inventories: List[Inventory],
) -> None:
    for report_class in [SimpleReport, CompleteReport]:
        for inventory in inventories:
            report = report_class()
            report.add_inventory(inventory)
            result = report.generate()
            assert f"Oldest manufacturing date: {OLDEST_DATE}" in result
