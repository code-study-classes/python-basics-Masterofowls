def check_between_numbers(a, b, c):
    return (a < b < c) or (c < b < a)


def check_odd_three(n):
    return 99 < abs(n) < 1000 and abs(n) % 2 == 1


def check_unique_digits(n):
    return (
    99 < abs(n) < 1000 and len(set(str(abs(n)))) == 3
)


def check_palindrome_number(n):
    return str(abs(n)) == str(abs(n))[::-1]


def check_ascending_digits(n):
    return (
    all(map(lambda x: x[0] < x[1], 
            zip(map(int, str(abs(n))), map(int, str(abs(n))[1:]))))
    if 99 < abs(n) < 1000 else False
)