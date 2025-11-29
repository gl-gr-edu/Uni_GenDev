array= [1, 2, 3, 4, 5, 6, 7]

def remove_elements(array, *items):
    for item in items:
        while item in array:
            array.remove(item)

if __name__ == "__main__":
    remove_elements(array, 5, 1, 6)
    print(array)