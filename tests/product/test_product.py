from inventory_report.product import Product


def test_create_product():
    product = Product(
        id="123",
        company_name="Company A",
        product_name="Product X",
        manufacturing_date="2022-01-01",
        expiration_date="2023-01-01",
        serial_number="SN123",
        storage_instructions="Store in a cool place",
    )

    assert product.id == "123"

    assert product.company_name == "Company A"

    assert product.product_name == "Product X"

    assert product.manufacturing_date == "2022-01-01"

    assert product.expiration_date == "2023-01-01"

    assert product.serial_number == "SN123"

    assert product.storage_instructions == "Store in a cool place"
