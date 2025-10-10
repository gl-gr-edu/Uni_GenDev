def count_types(data):
    type_counts = {}
    for item in data:
        t = type(item).__name__
        type_counts[t] = type_counts.get(t, 0) + 1
    return type_counts

if __name__ == "__main__":
    data = [True, 'hello', 5, 12, -200, False, False, 'word',99.99]
    result = count_types(data)
    for t, count in result.items():
        print(f"{t}: {count}")
