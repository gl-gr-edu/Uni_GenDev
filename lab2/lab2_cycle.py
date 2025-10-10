def range(start, stop):
    mas = []
    count = start
    while count <= stop:
        mas.append(count)
        count += 1
    print (mas)

def rangeOdd(start, stop):
    mas = []
    count = start
    while count <= stop:
        if count % 2 != 0:
            mas.append(count)
        count += 1
    print (mas)

if __name__ == "__main__":
    range(15,30)
    rangeOdd(15, 30)
