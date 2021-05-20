def uppercase(function):
    def wrapper(*args, **kwargs):
        return_val = function(*args, **kwargs)
        if isinstance(return_val, str):
            return_val = return_val.upper()
        else:
            print('Value not an instance of string')
        return return_val
    return wrapper


@uppercase
def greet(name):
    return f'Greetings {name}!'


if __name__ == "__main__":
    print(greet('World'))
