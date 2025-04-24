from functools import reduce


def find_common_elements(set1, set2):
    return set(filter(lambda x: x in set2, set1))


def is_superset(set_a, set_b):
    return all(map(lambda x: x in set_a, set_b))


def remove_duplicates(items):
    return reduce(
    lambda acc, x: acc + ([x] if x not in acc else []),
    items,
    []
)


def count_unique_words(text):
    return len(set(text.lower().split())) if text else 0


def find_shared_items(*sets):
    return (
    set() if not sets else
    reduce(lambda acc, s: set(filter(lambda x: x in s, acc)), sets[1:], sets[0])
)