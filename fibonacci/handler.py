def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def handle(req):
    try:
        n = int(req)
        result = fibonacci(n)
        return f"The {n}-th number in the Fibonacci sequence is {result}."
    except ValueError:
        return "Please provide an integer value."
