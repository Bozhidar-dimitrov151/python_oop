def tags(string):
    def decorator(func):
        def wrapped(*args):
            result = func(*args)
            wrap_result = f'<{string}>{result}</{string}>'
            return wrap_result
        return wrapped
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
