matrix_py = [
    [10, 5, 8],
    [12, 99, 3],
    [7, 15, 20]
]

def find_max(matrix):
    max_el= matrix[0][0]
    for row in matrix:
        for element in row:
            if element > max_el:
                max_el = element
    return max_el

if __name__ == '__main__':
    max_py = find_max(matrix_py)
    print(max_py)