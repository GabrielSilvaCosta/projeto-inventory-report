from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Product:
    id: str
    product_name: str
    company_name: str
    manufacturing_date: str
    expiration_date: str
    serial_number: str
    storage_instructions: str

    def expiration_date_valid(self) -> bool:
        today = date.today()
        expiration_date = datetime.strptime(
            self.expiration_date, "%Y-%m-%d"
        ).date()
        return expiration_date > today

    def __str__(self) -> str:
        return (
            f"The product {self.id} - {self.product_name} "
            f"with serial number {self.serial_number} "
            f"manufactured on {self.manufacturing_date} "
            f"by the company {self.company_name} "
            f"valid until {self.expiration_date} "
            "must be stored according to the following instructions: "
            f"{self.storage_instructions}."
        )
