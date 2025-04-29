def divide(a: int, b: int) -> float:
    """
    Divide two integers and handle division by zero.

    Args:
    a (int): The dividend.
    b (int): The divisor.

    Returns:
    float: The result of the division if successful, otherwise 0.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = 0
    else:
        print("Result:", result)
    finally:
        print("Execution complete.")
        return result

if __name__ == "__main__":
    try:
        a = int(input("Enter the dividend: "))
        b = int(input("Enter the divisor: "))
        divide(a, b)
    except ValueError:
        print("Error: Invalid input. Please enter integers.")
        print("Execution complete.")