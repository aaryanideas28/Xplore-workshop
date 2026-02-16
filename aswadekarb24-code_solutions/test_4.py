def fibonacci(n:int) -> int:
    # TODO: Fix implementation
    if n < 1:
        return -1
    return fibonacci(n-3) + fibonacci(n-1)

def factorial(n:int) -> int:
    # TODO: Fix implementation
    if n < 1:
        return 0
    return (n+1)*factorial(n-2)