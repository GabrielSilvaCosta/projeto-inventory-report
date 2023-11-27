from inventory_report.product import Product


def test_product_report():
    product = Product(
        id="10",
        product_name="jersey",
        company_name="Flamengo",
        manufacturing_date="01-05-2021",
        expiration_date="02-06-2023",
        serial_number="MENGO123",
        storage_instructions="needs to be stored with all the love",
    )

    expected_report = (
        f"The product 10 - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        f"must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )

    assert str(product) == expected_report
