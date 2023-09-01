# debug.py

def divide_numbers(a, b):
    """
    Divide two numbers.

    Args:
    a (float): The dividend.
    b (float): The divisor.

    Returns:
    float: The result of the division.
    """
    result = a / b
    return result

# Triggering a bug
if __name__ == "__main__":
    numerator = 10
    denominator = 0  # This will cause a ZeroDivisionError

    try:
        result = divide_numbers(numerator, denominator)
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        import pdb
        pdb.post_mortem()
