import pytest
from functions import (
    calculate_discount,
    filter_products,
    sort_products,
    validate_email
)

# --- Tests for calculate_discount ---

def test_calculate_discount_valid():
    assert calculate_discount(1000, 20) == 800.0

def test_calculate_discount_zero_discount():
    assert calculate_discount(500, 0) == 500.0

def test_calculate_discount_invalid_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)

def test_calculate_discount_invalid_discount_above_100():
    with pytest.raises(ValueError):
        calculate_discount(100, 120)


# --- Tests for filter_products ---

def test_filter_products_valid_query():
    products = [{"name": "Laptop", "price": 1000}, {"name": "Phone", "price": 500}]
    result = filter_products(products, "lap")
    assert result == [{"name": "Laptop", "price": 1000}]

def test_filter_products_empty_result():
    products = [{"name": "Laptop", "price": 1000}]
    assert filter_products(products, "xyz") == []

def test_filter_products_invalid_input():
    with pytest.raises(ValueError):
        filter_products("not-a-list", "query")


# --- Tests for sort_products ---

def test_sort_products_by_price():
    products = [
        {"name": "Laptop", "price": 1000},
        {"name": "Phone", "price": 500}
    ]
    result = sort_products(products, "price")
    assert result[0]["name"] == "Phone"

def test_sort_products_by_name():
    products = [
        {"name": "Laptop", "price": 1000},
        {"name": "Phone", "price": 500}
    ]
    result = sort_products(products, "name")
    assert result[0]["name"] == "Laptop"

def test_sort_products_invalid_key():
    with pytest.raises(ValueError):
        sort_products([], "invalid")


# --- Tests for validate_email ---

def test_validate_email_valid():
    assert validate_email("test@example.com")

def test_validate_email_invalid_format():
    assert not validate_email("invalid@com")

def test_validate_email_non_string():
    with pytest.raises(ValueError):
        validate_email(12345)
