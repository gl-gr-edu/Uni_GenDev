def store(value):
    def read():
        return value
    return read
if __name__ == "__main__":
    read = store(5)
    value = read()
    print(value)
