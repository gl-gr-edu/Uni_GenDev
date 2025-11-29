array1 = [1, 2, 3, 4, 5, 6, 7]
array2 = ['Kiev', 'Beijing', 'Lima', 'Saratov']

def removeElement(array, item):
    try:
        array.remove(item)
    except ValueError:
        pass

if __name__ == "__main__":
    removeElement(array1, 5)
    print(array1)
    removeElement(array2, 'Lima')
    removeElement(array2, 'Berlin')
    print(array2)