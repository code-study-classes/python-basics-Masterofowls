import pytest

from practice_package.branching import (
    convert_to_meters,
    describe_age,
    describe_number,
    get_discount,
    is_weekend,
)


class TestBranchingFunctions:
    @pytest.mark.parametrize(
        "day, expected",
        [
            (1, False),
            (6, True),
            (7, True),
            (5, False),
            (0, False),
            (8, False),
        ],
        ids=["monday", "saturday", "sunday", "friday", "zero", "invalid_day"],
    )
    def test_is_weekend(self, day, expected):
        assert is_weekend(day) == expected

    @pytest.mark.parametrize(
        "amount, expected",
        [
            (5500, 550),
            (1500, 75),
            (500, 0),
            (5000, 500),
            (999, 0),
            (1000, 50),
            (4999, 249.95),
        ],
        ids=[
            "high_discount",
            "medium_discount",
            "no_discount",
            "border_high",
            "border_low",
            "border_medium",
            "fractional",
        ],
    )
    def test_get_discount(self, amount, expected):
        assert get_discount(amount) == expected

    @pytest.mark.parametrize(
        "number, expected",
        [
            (24, "четное двузначное число"),
            (137, "нечетное трехзначное число"),
            (5, "нечетное однозначное число"),
            (100, "четное трехзначное число"),
            (999, "нечетное трехзначное число"),
            (0, "четное однозначное число"),
        ],
        ids=[
            "even_2digit",
            "odd_3digit",
            "odd_1digit",
            "even_3digit",
            "max_3digit",
            "zero",
        ],
    )
    def test_describe_number(self, number, expected):
        assert describe_number(number) == expected

    @pytest.mark.parametrize(
        "unit, length, expected",
        [
            (3, 10, 10),
            (1, 5, 0.5),
            (5, 2000, 20),
            (2, 1.5, 1500),
            (4, 1000, 1),
            (3, 0, 0),
        ],
        ids=[
            "meters",
            "decimeters",
            "centimeters",
            "kilometers",
            "millimeters",
            "zero_length",
        ],
    )
    def test_convert_to_meters(self, unit, length, expected):
        assert convert_to_meters(unit, length) == expected

    @pytest.mark.parametrize(
        "age, expected",
        [
            (20, "двадцать лет"),
            (32, "тридцать два года"),
            (41, "сорок один год"),
            (25, "двадцать пять лет"),
            (30, "тридцать лет"),
            (100, "сто лет"),
            (21, "двадцать один год"),
        ],
        ids=["20", "32", "41", "25", "30", "100", "21"],
    )
    def test_describe_age(self, age, expected):
        assert describe_age(age) == expected
