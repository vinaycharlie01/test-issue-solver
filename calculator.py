def divide(a, b):
    """Divide two numbers."""
    return a / b

def calculate(operation, a, b):
    """Perform calculation."""
    if operation == 'divide':
        return divide(a, b)
    elif operation == 'add':
        return a + b
    return None

def main():
    result = calculate('divide', 10, 0)  # Bug: will crash!
    print(f"Result: {result}")

if __name__ == "__main__":
    main()