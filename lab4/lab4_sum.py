from functools import reduce


def sum_index(*args):
    total=0
    for i in range(len(args)):
        total += args[i]
    return total



def sum_value(*args):
    total = 0
    for num in args:
        total += num
    return total

def sum_while(*args):
    total = 0
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total


def sum_do_while(*args):
    total = 0
    i = 0
    if len(args) == 0:
        return 0
    while True:
        total += args[i]
        i += 1
        if not (i < len(args)):
            break

    return total

def sum_reduce(*args):
    if not args:
        return 0
    return reduce(lambda accumulator, current_value: accumulator + current_value, args)

if __name__ == '__main__':
    print('sum_index(1, 2, 3):', sum_index(1, 2, 3))
    print('sum_value(0):', sum_value(0))
    print('sum_while():', sum_while())
    print('sum_do_while(1, -1, 1):', sum_do_while(1, -1, 1))
    print('sum_reduce(10, -1, -1, -1):', sum_reduce(10, -1, -1, -1))
    print('sum_reduce():', sum_reduce())
