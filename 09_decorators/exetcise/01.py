def logged(function):

    def wrapped(*args):
        result = function(*args)
        function_name_str = str(function.__name__)
        func_args = ", ".join(map(str, args))
        log_result = "you called " + function_name_str + "(" + func_args + ")" + '\n' + "it returned " + str(result)
        return log_result

    return wrapped

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))