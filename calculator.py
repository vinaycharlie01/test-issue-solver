def divide(num1, num2):
    """
    Divide two numbers and return the result.
    
    Args:
        num1 (float): The dividend.
        num2 (float): The divisor.
    
    Returns:
        float: The result of the division.
    """
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2

# Error handling added to prevent division by zero