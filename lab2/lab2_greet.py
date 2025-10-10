class Person:
    BIRTH_YEAR = 2007
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name)


if __name__ == "__main__":
    me = Person("Глеб")
    me.greet()