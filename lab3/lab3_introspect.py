import inspect

def introspect_object(obj):
    result = []
    for name, value in obj.items():
        if callable(value):
            sig = inspect.signature(value)
            result.append([name, len(sig.parameters)])
    return result

if __name__ == "__main__":
    iface = {
        "m1": lambda x: [x],
        "m2": lambda x, y: [x, y],
        "m3": lambda x, y, z: [x, y, z],
    }

    print(introspect_object(iface))