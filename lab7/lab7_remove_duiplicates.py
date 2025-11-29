def unique(array):
    seen = set()
    result = []
    for item in array:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == "__main__":
    result1 = unique([2, 1, 1, 3, 2])
    print(result1)
    result2 = unique(['top', 'bottom', 'top', 'left'])
    print(result2)

