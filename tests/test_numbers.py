import pytest

from practice_package.numbers import (
    calculate_digit_sum,
    calculate_distance,
    calculate_rect_area,
    calculate_segments,
    round_to_multiple,
)


class TestNumbersFunctions:
    @pytest.mark.parametrize(
        "x1, x2, expected",
        [
            (0, 5, 5),
            (-3, 2, 5),
            (5, 5, 0),
            (1.5, 3.5, 2.0),
            (-2.5, 2.5, 5.0),
        ],
        ids=["positive", "negative", "equal", "float", "negative_to_positive"],
    )
    def test_calculate_distance(self, x1, x2, expected):
        assert calculate_distance(x1, x2) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 3, 3),
            (15, 4, 3),
            (20, 5, 4),
            (1, 1, 1),
            (2, 1, 2),
        ],
        ids=["basic", "remainder", "exact", "equal", "double"],
    )
    def test_calculate_segments(self, a, b, expected):
        assert calculate_segments(a, b) == expected

    @pytest.mark.parametrize(
        "number, expected",
        [
            (47, 11),
            (-5, 5),
            (1000002, 3),
            (0, 0),
            (999, 27),
        ],
        ids=["2digit", "negative", "large", "zero", "all_nines"],
    )
    def test_calculate_digit_sum(self, number, expected):
        assert calculate_digit_sum(number) == expected

    @pytest.mark.parametrize(
        "coords, expected",
        [
            ((0, 0, 5, 3), 15),
            ((2, 2, 2, 5), 0),
            ((-1, -1, 2, 4), 15),
            ((0, 0, 0, 0), 0),
        ],
        ids=["normal", "degenerate", "negative_coords", "zero_area"],
    )
    def test_calculate_rect_area(self, coords, expected):
        x1, y1, x2, y2 = coords
        assert calculate_rect_area(x1, y1, x2, y2) == expected

    @pytest.mark.parametrize(
        "number, multiple, expected",
        [
            (10, 6, 12),
            (-13, 5, -15),
            (15, 7, 14),
            (10, 3, 9),
            (0, 5, 0),
        ],
        ids=["round_up", "negative", "round_down", "equal_distance", "zero"],
    )
    def test_round_to_multiple(self, number, multiple, expected):
        assert round_to_multiple(number, multiple) == expected
