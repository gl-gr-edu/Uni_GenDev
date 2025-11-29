persons = {
    'lenin': {'born': 1870, 'died': 1924},
    'mao': {'born': 1893, 'died': 1976},
    'gandhi': {'born': 1869, 'died': 1948},
    'hirohito': {'born': 1901, 'died': 1989},
}

def calculate_ages(persons):
    ages = {}
    for person_name in persons:
        dates = persons[person_name]
        born_year = dates['born']
        died_year = dates['died']
        lifespan = died_year - born_year
        ages[person_name] = lifespan
    return ages

if __name__ == '__main__':
    result = calculate_ages(persons)
    print(result)