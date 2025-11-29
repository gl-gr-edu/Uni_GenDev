class Seq:
    def __init__(self, initial_func=None):
        self.functions = []
        if initial_func:
            self.functions.append(initial_func)

    def __call__(self, arg):
        if callable(arg):
            self.functions.append(arg)
            return self

        if isinstance(arg, (int, float)):
            result = arg
            for func in self.functions:
                result = func(result)
            return result
        raise TypeError("The argument must be a function or a number")

def seq(initial_func):
    return Seq(initial_func)

if __name__ == '__main__':
    result1 = seq(lambda x: x + 7)(lambda x: x * 2)(5)
    print(result1)
    result2 = seq(lambda x: x * 2)(lambda x: x + 7)(5)
    print(result2)
    result3 = seq(lambda x: x + 1)(lambda x: x * 2)(lambda x: x / 3)(lambda x: x - 4)(7)
    print(result3)