def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Raises TypeError if input is not a number.
    """
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Temperature must be an integer or a float.")
        
    return (fahrenheit - 32) * 5.0 / 9.0


def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    n = 0 -> 0, n = 1 -> 1, etc.
    Raises TypeError if n is not an integer.
    Raises ValueError if n is negative.
    """
    if not isinstance(n, int) or isinstance(n, bool): 
        raise TypeError("Index n must be an integer.")
    if n < 0:
        raise ValueError("Index n cannot be negative.")
        
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b