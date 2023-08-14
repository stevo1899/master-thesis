
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def handle(req):
    try:
        n = int(req)
        result = factorial(n)
        return f"The factorial of {n} is {result}."
    except ValueError:
        return "Please provide an integer value."

