class FunctionalArray:
    def __init__(self):
        self._array = []

    def __call__(self, index):
        if 0 <= index < len(self._array):
            return self._array[index]
        return None

    def push(self, value):
        self._array.append(value)

    def pop(self):
        if self._array:
            return self._array.pop()
        return None

def array():
    return FunctionalArray()
if __name__ == '__main__':
    arr = array()
    arr.push('first')
    arr.push('second')
    arr.push('third')
    print(arr(0))
    print(arr(1))
    print(arr(2))
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())