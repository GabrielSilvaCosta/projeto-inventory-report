from abc import ABC, abstractmethod
import csv
import json
from typing import Dict, Type, List
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as json_file:
            data = json.load(json_file)

        return [
            Product(
                id=item["id"],
                product_name=item["product_name"],
                company_name=item["company_name"],
                manufacturing_date=item["manufacturing_date"],
                expiration_date=item["expiration_date"],
                serial_number=item["serial_number"],
                storage_instructions=item["storage_instructions"],
            )
            for item in data
        ]


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        return [
            Product(
                id=item["id"],
                product_name=item["product_name"],
                company_name=item["company_name"],
                manufacturing_date=item["manufacturing_date"],
                expiration_date=item["expiration_date"],
                serial_number=item["serial_number"],
                storage_instructions=item["storage_instructions"],
            )
            for item in data
        ]


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
