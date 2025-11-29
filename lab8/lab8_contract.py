def contract(fn, *types):
    def wrapper(*args):
        for arg, expected in zip(args, types[:-1]):
            if not isinstance(arg, expected):
                raise TypeError("Unexpected type")
        result = fn(*args)
        if not isinstance(result, types[-1]):
            raise TypeError("Unexpected type")
        return result
    return wrapper

def add(a, b):
    return a + b

def concat(s1, s2):
    return s1 + s2
if __name__ == "__main__":
    add_numbers = contract(add, int, int, int)
    print(add_numbers(2, 3))
    concat_strings = contract(concat, str, str, str)
    print(concat_strings('Hello ', 'world!'))
