from unittest import result


def average(x,y):
    return (x + y) / 2

def square(x):
    return x**2

def cube(x):
    return x**3

def calculate(x,y):
    result = []
    for i in range(x,y):
        num = average(square(i),cube(i))
        result.append(num)
    return result


if __name__ == "__main__":
    print(calculate(0,9))


