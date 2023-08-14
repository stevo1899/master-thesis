def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def handle(req):
    try:
        n = int(req)
        result = is_prime(n)
        if result:
            return f'{n} is a prime number.'
        else:
            return f'{n} is not a prime number.'
    except ValueError:
        return 'Please provide an integer value.'
