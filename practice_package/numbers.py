def calculate_distance(x1, x2):
    return abs(x1 - x2)


def calculate_segments(a, b):
    return a // b


def calculate_digit_sum(number):
    return sum(int(d) for d in str(abs(number)))


def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)


def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)