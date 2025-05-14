# Andreas Xeni, U244N0653

# Task 1
def add(a, b):
    """
    Add two numbers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract one number from another.

    Parameters:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.

    Returns:
        int or float: The result of a - b.
    """
    return a - b

# Task 2
def is_even(n):
    """
    Check if a number is even.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

# Task 3
def reverse_string(s):
    """
    Reverse the given string.

    Parameters:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

# Task 4
def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Parameters:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower()
    return s == s[::-1]

# Task 5
def max_numbers(numbers):
    """
    Return the maximum number from a list.

    Parameters:
        numbers (list of int or float): A list of numbers.

    Returns:
        int or float: The maximum number in the list.
    """
    return max(numbers)

# Task 6
def factorial(n):
    """
    Compute the factorial of a non-negative integer.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("no factorial for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Task 7
def sort_numbers(numbers):
    """
    Sort a list of numbers in ascending order.

    Parameters:
        numbers (list of int or float): The numbers to sort.

    Returns:
        list: A sorted list of numbers.
    """
    return sorted(numbers)

# Task 8
def is_valid_password(password):
    """
    Check if a password is valid.

    A valid password must be at least 8 characters long and contain
    at least one uppercase letter, one lowercase letter, and one digit.

    Parameters:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_digit and has_lower and has_upper
