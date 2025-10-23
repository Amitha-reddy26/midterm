from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide
import pytest

fake = Faker()

operation_mappings = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

def generate_test_data(num_records):
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        if operation_func == divide and b == 0:
            b = Decimal('1')
        expected = operation_func(a, b)
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        test_data = list(generate_test_data(num_records))
        metafunc.parametrize("a,b,operation_name,expected", test_data)

def test_generate_test_data():
    test_data = list(generate_test_data(5))
    assert len(test_data) == 5
    for _, _, operation_name, _, _ in test_data:
        assert operation_name in operation_mappings

def test_operation_with_negatives():
    assert add(3, -2) == 1
    assert subtract(-3, -2) == -1
    assert multiply(-3, 3) == -9
    assert divide(-6, 2) == -3

def test_large_numbers():
    assert add(Decimal('1e6'), Decimal('1e6')) == Decimal('2e6')
    assert subtract(Decimal('1e6'), Decimal('1')) == Decimal('999999')
    assert multiply(Decimal('1e3'), Decimal('1e3')) == Decimal('1e6')
    assert divide(Decimal('1e6'), Decimal('1e3')) == Decimal('1000')

def test_edge_cases():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(Decimal('1'), Decimal('0'))
    assert add(Decimal('0'), Decimal('0')) == Decimal('0')
    assert subtract(Decimal('0'), Decimal('0')) == Decimal('0')
