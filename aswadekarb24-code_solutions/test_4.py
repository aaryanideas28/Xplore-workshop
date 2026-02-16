def fibonacci(n:int) -> int:
    # TODO: Fix implementation
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def factorial(n:int) -> int:
    # TODO: Fix implementation
    if n < 1:
        return 1
    return (n)*factorial(n-1)