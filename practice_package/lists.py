from functools import reduce


def square_odds(numbers):
    return list(map(
    lambda x: x * x, 
    filter(lambda x: x % 2 != 0, numbers)
))


def normalize_names(names):
    return list(map(str.capitalize, names))


def remove_invalid_emails(emails):
    return list(filter(
    lambda email: (
        len(email) >= 5 and 
        email.count('@') == 1 and 
        not email.startswith('@') and 
        not email.endswith('@')
    ),
    emails
))


def filter_palindromes(words):
    return list(filter(
    lambda w: w.lower() == w.lower()[::-1], 
    words
))


def calculate_factorial(n):
    return (
    1 if n <= 1 else 
    reduce(lambda x, y: x * y, range(1, n + 1))
)


def find_common_prefix(strings):
    return (
    "" if not strings else 
    reduce(
        lambda acc, pair: acc[:pair[0]] if pair[1][0] != pair[1][1] else acc,
        enumerate(zip(min(strings), max(strings))),
        min(strings)
    )
)