def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fibonacci(n-1, b, a + b)
