def cache(func):
    def wrapped(param):
        if not wrapped.log.get(param):
            wrapped.log[param] = func(param)

        return wrapped.log[param]

    wrapped.log = {}

    return wrapped


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)