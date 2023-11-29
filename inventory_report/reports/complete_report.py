from datetime import datetime

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        oldest_manufacturing_date = self.get_oldest_date("manufacturing_date")
        closest_expiration_date = self.get_oldest_date("expiration_date", True)
        largest_inventory_company = self.get_largest_inventory_company()
        stocked_products_by_company = self.get_stocked_products_by_company()

        result = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory:{largest_inventory_company}\n"
            "Stocked products by company:"
        )

        for company, count in stocked_products_by_company.items():
            result += f"\n- {company}: {count}"

        return result

    def get_stocked_products_by_company(self) -> dict:
        stocked_products_by_company = {}
        for inventory in self.inventories:
            for product in inventory.data:
                if self.product_is_stocked(product):
                    stocked_products_by_company[product.company_name] = (
                        stocked_products_by_company.get(
                            product.company_name, 0
                        )
                        + 1
                    )

        return stocked_products_by_company

    def product_is_stocked(self, product) -> bool:
        return (
            datetime.strptime(product.expiration_date, "%Y-%m-%d").date()
            > datetime.strptime(
                self.get_oldest_date("expiration_date", True), "%Y-%m-%d"
            ).date()
        )
