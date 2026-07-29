def make_bold(function):
    def wrapped(*args):
        result = function(*args)
        wrap_result = "<b>" + result + "</b>"
        return wrap_result
    return wrapped

def make_italic(function):
    def wrapped(*args):
        result = function(*args)
        wrap_result = "<i>" + result + "</i>"
        return wrap_result

    return wrapped

def make_underline(function):
    def wrapped(*args):
        result = function(*args)
        wrap_result = "<u>" + result + "</u>"
        return wrap_result

    return wrapped

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

