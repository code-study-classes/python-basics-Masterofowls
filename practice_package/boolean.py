def check_between_numbers(a, b, c):
    return (a < b < c) or (c < b < a)


def check_odd_three(n):
    return 99 < abs(n) < 1000 and abs(n) % 2 == 1


def check_unique_digits(n):
    return ((99 < abs(n) < 1000) and 
            len(set(str(abs(n)))) == 3)


def check_palindrome_number(n):
    s = str(abs(n))
    return s == s[::-1]


def check_ascending_digits(n):
    if not (99 < abs(n) < 1000):
        return False
    digits = str(abs(n))
    return all(int(d1) < int(d2) for d1, d2 in zip(digits, digits[1:]))