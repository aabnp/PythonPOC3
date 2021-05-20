registry = []


def register(function):
    global registry

    def wrapper(*args, **kwargs):
        return_val = function(*args, **kwargs)
        registry.append(function.__name__)
        return return_val
    return wrapper


def greet(name):
    return f'Greetings {name}!'


@register
def say_hello(name):
    return f'Hello {name}!'


@register
def say_goodbye(name):
    return f'Goodbye {name}!'


if __name__ == "__main__":
    greet('World')
    say_hello('World')
    say_goodbye('World')
    print(registry)
