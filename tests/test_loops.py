import pytest

from practice_package.loops import (
    count_vowel_triplets,
    find_fibonacci_index,
    remove_duplicates,
    sum_even_digits,
)


class TestLoopsFunctions:
    """Test loop-based functions.

    Notes on vowel triplet handling:
    - A triplet is any 3 consecutive vowels (a,e,i,o,u)
    - 'y' is only counted in the sequence 'yyy'
    - Overlapping sequences count separately if they don't share more than
      1 vowel:
      e.g., "Queueing" -> "uee" and "eei" count as 2 triplets
      but "AeIoU" -> counts as 1 triplet since they all form one group
    """

    @pytest.mark.parametrize(
        "number, expected",
        [
            (123456, 12),
            (-13579, 0),
            (2468, 20),
            (0, 0),
            (13579, 0),
            (-2468, 20),
            (111122, 4),
        ],
        ids=[
            "mixed",
            "all_odd",
            "all_even",
            "zero",
            "all_odd_positive",
            "all_even_negative",
            "with_duplicates",
        ],
    )
    def test_sum_even_digits(self, number, expected):
        assert sum_even_digits(number) == expected

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("Beautiful day", 1),  # eau = 1 triplet
            ("Queueing", 2),  # uee, eei = 2 triplets (overlapping allowed)
            ("Python", 0),  # no triplets (y not counted)
            ("AeIoU", 1),  # counts as 1 continuous triplet
            ("", 0),  # empty string
            ("YyY", 1),  # special case: yyy counts as triplet
            ("Hello world", 0),  # no triplets
        ],
        ids=[
            "normal",
            "double",
            "no_vowels",
            "all_vowels",
            "empty",
            "only_y",
            "spaces",
        ],
    )
    def test_count_vowel_triplets(self, text, expected):
        assert count_vowel_triplets(text) == expected

    @pytest.mark.parametrize(
        "number, expected",
        [
            (8, 6),
            (610, 15),
            (4, -1),
            (1, 1),
            (2, 3),
            (144, 12),
            (987, 16),
        ],
        ids=[
            "small",
            "medium",
            "not_fib",
            "first",
            "second",
            "twelfth",
            "large",
        ],
    )
    def test_find_fibonacci_index(self, number, expected):
        assert find_fibonacci_index(number) == expected

    @pytest.mark.parametrize(
        "string, expected",
        [
            ("aaabbbccca", "abca"),
            ("abcde", "abcde"),
            ("112233311", "1231"),
            ("", ""),
            ("aaaaa", "a"),
            ("ababab", "ababab"),
            ("HHeellloo", "Helo"),
        ],
        ids=[
            "basic",
            "no_duplicates",
            "numbers",
            "empty",
            "all_same",
            "alternating",
            "mixed_case",
        ],
    )
    def test_remove_duplicates(self, string, expected):
        assert remove_duplicates(string) == expected
