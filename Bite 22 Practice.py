from functools import wraps

def make_html(element):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return f'<{element}>{function(*args, **kwargs)}</{element}>'
        return wrapper
    return inner_function