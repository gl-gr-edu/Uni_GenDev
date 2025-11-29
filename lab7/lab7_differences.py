def difference(array1, array2):
    result = []
    for item in array1:
        if item not in array2:
            result.append(item)
    return result

if __name__ == "__main__":
    print(difference([1, 2, 3, 4, 5], [2, 4]))
    print(difference(['apple', 'banana', 'cherry'], ['banana', 'date']))
