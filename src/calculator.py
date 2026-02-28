def calculate_divide(a, b):
    """Calculate division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_remainder(a, b):
    """Calculate remainder of division."""
    if b == 0:
        raise ValueError("Cannot calculate remainder by zero")
    return a % b
