import random
from xml.dom.pulldom import CHARACTERS

CHARACTERS='abcdefghijklmnopqrstuvwxyz0123456789'

def randomizer(min_value,max_value=None):
    if max_value is None:
        max_value = min_value
        min_value = 0
    return random.randint(min_value,max_value)

def generateKey(length):
    key = ''
    for _ in range(length):
        key += random.choice(CHARACTERS)
    return key


if __name__ == "__main__":
    print(randomizer(0,100))
    print(randomizer(50))
    key = generateKey(10)
    print(key)
