import pytest
from freezegun import freeze_time
from app.main import outdated_products
import datetime


@pytest.fixture
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        },
    ]


@freeze_time("2022-02-02")  # Mock today's date to 2 February 2022
def test_outdated_products_today(products: list) -> None:
    assert outdated_products(products) == ["duck"]


@freeze_time("2022-02-05")  # Mock today's date to 5 February 2022
def test_outdated_products_past(products: list) -> None:
    assert outdated_products(products) == ["duck"]


@freeze_time("2022-02-12")  # Mock today's date to 12 February 2022
def test_outdated_products_future(products: list) -> None:
    assert outdated_products(products) == ["salmon", "chicken", "duck"]
