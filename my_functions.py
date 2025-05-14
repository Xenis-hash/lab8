#Andreas Xeni, U244N0653

#Task 1
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

#Task 2
def is_even(n):
    return n%2==0

#Task 3
def reverse_string(s):
    return s[::-1]

#Task 4
def is_palindrome(s):
    s=s.lower()
    return s==s[::-1]
#Task 5
def max_numbers(numbers):
    return max(numbers)

#Task 6
def factorial(n):
    if n<0:
        raise ValueError("no factorial for negative numbers.")
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

#Task 7
def sort_numbers(numbers):
    return sorted(numbers)

#Task 8
def is_valid_password(password):
    if len(password)<8:
        return False
    has_upper=any(char.isupper() for char in password)
    has_lower=any(char.islower() for char in password)
    has_digit=any(char.isdigit()for char in password)
    return has_digit and has_lower and has_upper    