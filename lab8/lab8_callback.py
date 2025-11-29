obj = {'a': 1, 'b': 2, 'c': 3}

def iterate(obj, callback):
    for key, value in obj.items():
        callback(key, value, obj)

if __name__ == "__main__":
    iterate(obj, lambda key, value, obj: print({'key': key, 'value': value}))

