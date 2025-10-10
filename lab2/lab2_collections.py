
phone_book_list = [
    {"name": "Marcus Aurelius", "phone": "+380445554433"},
    {"name": "Gleb", "phone": "+380994456789"},
    {"name": "Adam", "phone": "+380504567890"},
]

phone_book_hash = {
    "Marcus Aurelius": "+380445554433",
    "Seneca": "+380667778899",
    "Epictetus": "+380993334455",
}


def findPhoneByName_list(name):
    for i in phone_book_list:
        if i["name"] == name:
            return i["phone"]
    return "Номер не найден"

def findPhoneByName_hash(name):
    return phone_book_hash.get(name, "Номер не найден")


if __name__ == "__main__":
    print(findPhoneByName_list("Gleb"))
    print(findPhoneByName_list("Peter"))
    print(findPhoneByName_hash("Marcus Aurelius"))
    print(findPhoneByName_hash("Anatoliy"))
