def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base, exp):
    return base**exp


def mod(a, b):
    return a % b


def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def max_in_list(numbers):
    if not numbers:
        return None
    return max(numbers)


def min_in_list(numbers):
    if not numbers:
        return None
    return min(numbers)
