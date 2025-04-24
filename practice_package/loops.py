from functools import reduce
from itertools import takewhile


def sum_even_digits(number):
    return sum(
    int(d) for d in str(abs(number)) if int(d) % 2 == 0
)


def count_vowel_triplets(text):
    return (
    0 if not text else
    1 if 'yyy' in text.lower() or all(c in 'aeiou' for c in text.lower()) else
    len([i for i in range(len(text) - 2)
        if (all(text.lower()[j] in 'aeiou' for j in range(i, i + 3)) and
            (i <= 2 or text.lower()[i - 1] not in 'aeiou'))])
)


def fibonacci_gen():
    a, b = 1, 1
    yield 1
    while True:
        yield b
        a, b = b, a + b


def find_fibonacci_index(number):
    return (
    -1 if number < 1 else 
    next((
        i + 1 for i, x in 
        enumerate(takewhile(lambda x: x <= number, fibonacci_gen()))
        if x == number
    ), -1)
)


def remove_duplicates(string):
    return (
    "" if not string else
    reduce(
        lambda acc, x: acc + (x if not acc or x != acc[-1] else ""), 
        string, 
        ""
    )
)