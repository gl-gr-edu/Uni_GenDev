inc = lambda x: x + 1
twice = lambda x: x * 2
cube = lambda x: x ** 3

def pipe(*funcs):
    if not all(callable(f) for f in funcs):
        raise TypeError("All arguments must be functions")

    def composed(x):
        for f in funcs:
            x = f(x)
        return x

    return composed

if __name__ == "__main__":
    f = pipe(inc, twice, cube)
    print(f(5))
