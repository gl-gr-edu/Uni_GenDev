def compose_right(*funcs):
    if not all(callable(f) for f in funcs):
        raise TypeError("All arguments to compose_right must be callable")

    functions_if_error = []

    def composed(value):
        result = value
        for f in reversed(funcs):
            try:
                result = f(result)
            except Exception as e:
                for error_handler in functions_if_error:
                    error_handler(e)
                return None
        return result

    def on(event, error_handler):
        if event == "error" and callable(error_handler):
            functions_if_error.append(error_handler)

    composed.on = on
    return composed

f = compose_right(
    lambda x: x ** 3,
    lambda x: x + 1,
    lambda x: x * 2
)
def inc(x): return x + 1
def twice(x): return x * 2
def boom(x): raise ValueError("fail")

if __name__ == "__main__":
    f1=compose_right(lambda x: x ** 3,lambda x: x + 1,lambda x: x * 2)
    f2 = compose_right(inc, boom, twice)
    f2.on("error", lambda e: print("Error:", e))
    print(f1(5))
    print(f2(3))

