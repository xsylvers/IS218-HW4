from typing import Union, List

class Calculator:
    history: List[str] = []

    def __init__(self):
        pass

    @classmethod
    def add_calculation(cls, calculation: str) -> None:
        """This line of code adds a calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Union[str, None]:
        """This line of code retrevies the last calculation from history."""
        return cls.history[-1] if cls.history else None

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """This line of code returns the sum of two numbers."""
        result = a + b
        Calculator.add_calculation(f"Add: {a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """This line of code returns the difference of two numbers."""
        result = a - b
        Calculator.add_calculation(f"Subtract: {a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Thus line of code returns the product of two numbers."""
        result = a * b
        Calculator.add_calculation(f"Multiply: {a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """This line of code returns the quotient of two numbers, raise ZeroDivisionError if divisor is zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculator.add_calculation(f"Divide: {a} / {b} = {result}")
        return result
