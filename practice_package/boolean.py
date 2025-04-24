check_between_numbers = lambda a, b, c: (a < b < c) or (c < b < a)

check_odd_three = lambda n: 99 < abs(n) < 1000 and abs(n) % 2 == 1

check_unique_digits = lambda n: (99 < abs(n) < 1000) and len(set(str(abs(n)))) == 3

def check_palindrome_number(n):
    s = str(abs(n))
    return s == s[::-1]

check_ascending_digits = lambda n: (99 < abs(n) < 1000) and all(int(d1) < int(d2) for d1, d2 in zip(str(abs(n)), str(abs(n))[1:]))