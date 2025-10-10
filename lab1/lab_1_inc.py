class Number:

    @staticmethod
    def inc_value(n: int) -> int:
        return n + 1

    class ByReference:
        def __init__(self, n: int):
            self.n = n

    @staticmethod
    def inc(num):
        num.n += 1


if __name__ == "__main__":
    a = 5
    b = Number.inc_value(a)
    print({"a": a, "b": b})
    obj = Number.ByReference(5)
    Number.inc(obj)
    print({"n": obj.n})
