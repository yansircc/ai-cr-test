def calculate_sum(a, b):
    """Calculate sum of two numbers."""
    return a + b


def calculate_product(a, b):
    """Calculate product of two numbers."""
    return a * b


def calculate_average(numbers):
    """Calculate average of numbers."""
    return sum(numbers) / len(numbers)


def calculate_divide(a, b):
    """Divide two numbers."""
    return a / b


def main():
    print("Calculator App")
    print(calculate_sum(1, 2))
    print(calculate_product(3, 4))
    print(calculate_average([1, 2, 3, 4, 5]))
    print(calculate_divide(10, 0))


if __name__ == "__main__":
    main()
# trigger rebuild

