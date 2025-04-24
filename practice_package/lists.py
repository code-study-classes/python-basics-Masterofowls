def square_odds(numbers):
    return list(map(lambda x: x * x, filter(lambda x: x % 2 != 0, numbers)))


def normalize_names(names):
    return list(map(str.capitalize, names))


def remove_invalid_emails(emails):
    def is_valid_email(email):
        return (len(email) >= 5 and 
                email.count('@') == 1 and 
                not email.startswith('@') and 
                not email.endswith('@'))
    return list(filter(is_valid_email, emails))


def filter_palindromes(words):
    return list(filter(lambda w: w.lower() == w.lower()[::-1], words))


def calculate_factorial(n):
    from functools import reduce
    if n <= 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


def find_common_prefix(strings):
    if not strings:
        return ""
    first = min(strings)
    last = max(strings)
    for i, (c1, c2) in enumerate(zip(first, last)):
        if c1 != c2:
            return first[:i]
    return first