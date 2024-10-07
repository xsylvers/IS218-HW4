def perform_calculation(a, b, operation):
    """This line of code defines a simple function to perform basic calculations."""
    try:
        a = float(a)
        b = float(b)

        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            return a / b
        else:
            raise ValueError(f"Unsupported operation '{operation}'.")

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    print("Welcome to the my calculator program!")
    
    try:
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        operation = input("Enter the operation (+, -, *, /): ")

        result = perform_calculation(a, b, operation)
        print(f"Result: {result}")
    
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

