import pytest

from practice_package.boolean import (
    check_ascending_digits,
    check_between_numbers,
    check_odd_three,
    check_palindrome_number,
    check_unique_digits,
)


class TestBooleanFunctions:
    @pytest.mark.parametrize(
        "a, b, c, expected",
        [
            (1, 2, 3, True),
            (5, 5, 8, False),
            (10, 7, 5, True),
            (-5, 0, 5, True),
            (100, 150, 200, True),
            (1, 0, 2, False),
        ],
        ids=[
            "simple_true",
            "equal_false",
            "reverse_order",
            "negative_range",
            "large_numbers",
            "outside_range",
        ],
    )
    def test_check_between_numbers(self, a, b, c, expected):
        assert check_between_numbers(a, b, c) == expected

    @pytest.mark.parametrize(
        "number, expected",
        [
            (135, True),
            (246, False),
            (-789, True),
            (2458, False),
            (99, False),
            (-100, False),
            (999, True),
        ],
        ids=[
            "odd_positive",
            "even_positive",
            "odd_negative",
            "too_large",
            "too_small",
            "even_negative",
            "max_value",
        ],
    )
    def test_check_odd_three(self, number, expected):
        assert check_odd_three(number) == expected

    @pytest.mark.parametrize(
        "number, expected",
        [
            (123, True),
            (122, False),
            (-987, True),
            (-77, False),
            (1234, False),
            (111, False),
            (456, True),
        ],
        ids=[
            "all_unique",
            "duplicate",
            "negative_unique",
            "negative_duplicate",
            "not_3digit",
            "all_same",
            "another_unique",
        ],
    )
    def test_check_unique_digits(self, number, expected):
        assert check_unique_digits(number) == expected

    @pytest.mark.parametrize(
        "number, expected",
        [
            (121, True),
            (12321, True),
            (-121, True),
            (10, False),
            (123, False),
            (-1221, True),
            (0, True),
        ],
        ids=[
            "simple_palindrome",
            "long_palindrome",
            "negative_palindrome",
            "not_palindrome",
            "another_not",
            "negative_even",
            "zero",
        ],
    )
    def test_check_palindrome_number(self, number, expected):
        assert check_palindrome_number(number) == expected

    @pytest.mark.parametrize(
        "number, expected",
        [
            (123, True),
            (135, True),
            (321, False),
            (112, False),
            (99, False),
            (-789, True),
            (100, False),
        ],
        ids=[
            "ascending",
            "ascending_gaps",
            "descending",
            "duplicates",
            "not_3digit",
            "negative_ascending",
            "with_zero",
        ],
    )
    def test_check_ascending_digits(self, number, expected):
        assert check_ascending_digits(number) == expected
