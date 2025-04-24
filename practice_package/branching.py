def is_weekend(day):
    return day in (6, 7)


def get_discount(amount):
    return (
    round(amount * 0.1, 2) if amount >= 5000 else
    round(amount * 0.05, 2) if amount >= 1000 else 0
)


DIGITS_MAP = {1: 'однозначное', 2: 'двузначное', 3: 'трехзначное'}


def describe_number(n):
    return (
    f"{('четное' if n % 2 == 0 else 'нечетное')} "
    f"{DIGITS_MAP[len(str(n))]} число"
)


def convert_to_meters(unit_number, length_in_units):
    return length_in_units * {
    1: 0.1,       # дециметр
    2: 1000,      # километр
    3: 1,         # метр
    4: 0.001,     # миллиметр
    5: 0.01       # сантиметр
}[unit_number]


TENS_MAP = {
    2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
    6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто', 
    10: 'сто'
}
ONES_MAP = {
    0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
    5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
}
YEARS_MAP = {
    1: 'год', 2: 'года', 3: 'года', 4: 'года',
    5: 'лет', 6: 'лет', 7: 'лет', 8: 'лет', 9: 'лет', 0: 'лет'
}


def describe_age(age):
    return (
    'сто лет' if age == 100 else
    f"{TENS_MAP[age // 10]}" + 
    (f" {ONES_MAP[age % 10]}" if age % 10 != 0 else '') +
    f" {YEARS_MAP[age % 10]}"
)