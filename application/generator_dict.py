import random


NAMES = [
    'Андрей', 'Валерий', 'Антон',
    'Юрий', 'Сергей', 'Ирина',
    'Екатерина', 'Светлана', 'Надежда', 'Елена'
]

SURNAMES = [
    'Козловский', 'Савицкий', 'Аронов',
    'Котковский', 'Гуринович', 'Варшавский',
    'Цыганок', 'Карабко', 'Терпиловский', 'Музыченко'
]

PATRONYMICS = [
    'Дмитриевич', 'Анатольевич', 'Степанович',
    'Генадьевич', 'Васильевич','Андреевич',
    'Антонович', 'Сергеевич', 'Русланович', 'Максимович'
]

NUM_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year_or_not(y):
    return True if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else False


def days_in_month(y, m):
    if m == 2 and leap_year_or_not(y):
        return random.randint(1, 29)
    else:
        return random.randint(1, NUM_DAYS[m - 1])


def worker_dictionary_generator():
    workers = {}
    rand_value = random.randint(10, 30)
    for i in range(rand_value):
        number_name_in_list = random.randint(0, 9)
        name = NAMES[number_name_in_list]
        month = random.randint(1, 12)
        year = random.randint(1975, 2000)

        if number_name_in_list >= 5:  # Determine the gender of the worker by name in list (first five is men)
            surname = SURNAMES[random.randint(0,9)]
            if surname[-2:] == 'ий':
                surname = surname[:-2] + 'ая'
            elif surname[-1] == 'в':
                surname = surname + 'а'
            workers[i+1] = {
                'surname': surname,
                'name': name,
                'patronymics': PATRONYMICS[random.randint(0, 9)][:-2] + 'на',
                'date': f'{days_in_month(year, month)}.'
                        f'{month}.'
                        f'{year}',
                'sex': 'female'
            }
        else:
            workers[i+1] = {
                'surname': SURNAMES[random.randint(0,9)],
                'name': name,
                'patronymics': PATRONYMICS[random.randint(0, 9)],
                'date': f'{days_in_month(year, month)}.'
                        f'{month}.'
                        f'{year}',
                'sex': 'male'
            }

    return workers
