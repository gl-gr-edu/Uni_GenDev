ip = '127.0.0.1'

def ipv4_translator(address)
    nums = list(map(int, address.split('.')))
    value = 0
    for num in nums:
        value = (value << 8) + num
    if value >= 2**31:
        value -= 2**32
    return value

if __name__ == "__main__":
    print(f"{ip} -> {ipv4_translator(ip)}")

