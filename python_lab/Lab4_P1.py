def reverse_string(text: str) -> str:
    """
    Reverse the given string.

    Args:
    text (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """
    Check if the given string is a palindrome.

    Args:
    text (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return text == reverse_string(text)

if __name__ == "__main__":
    text = input("")
    print("True" if is_palindrome(text) else "False")