def fibonacci(n:int) -> int:
    # TODO: Fix implementation
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def factorial(n:int) -> int:
    # TODO: Fix implementation
    if n < 1:
        return 1
    return (n)*factorial(n-1)