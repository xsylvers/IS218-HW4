import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    """Add --num_records option to pytest."""
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

@pytest.fixture
def generate_test_data(request):
    """This is a fixture to generate dynamic test data."""
    num_records = request.config.getoption("--num_records")

    # Generate test data
    test_data = []
    for _ in range(num_records):
        a = fake.random_number(digits=3)
        b = fake.random_number(digits=3)
        operation = fake.random_element(elements=["+", "-", "*", "/"])
        
        # Fake expected result
        if operation == "+":
            expected_result = a + b
        elif operation == "-":
            expected_result = a - b
        elif operation == "*":
            expected_result = a * b
        else:  # Division case
            if b != 0:
                expected_result = a / b
            else:
                b = 1  # This line of code avoids division by zero
                expected_result = a / b

        test_data.append((a, b, operation, expected_result))

    return test_data
