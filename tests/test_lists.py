import pytest

from practice_package.lists import (
    calculate_factorial,
    filter_palindromes,
    find_common_prefix,
    normalize_names,
    remove_invalid_emails,
    square_odds,
)


class TestListsFunctions:
    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1, 2, 3, 4, 5], [1, 9, 25]),
            ([2, 4, 6], []),
            ([-3, 0, 3], [9, 9]),
            ([], []),
            ([-1, -2, -3], [1, 9]),
        ],
        ids=[
            "mixed",
            "all_even",
            "with_negative",
            "empty",
            "all_negative_odds",
        ],
    )
    def test_square_odds(self, numbers, expected):
        assert square_odds(numbers) == expected

    @pytest.mark.parametrize(
        "names, expected",
        [
            (["alice", "BOB", "chArLie"], ["Alice", "Bob", "Charlie"]),
            ([], []),
            (["john"], ["John"]),
            (["", " "], ["", " "]),
            (["a"], ["A"]),
        ],
        ids=["mixed_case", "empty", "single", "edge_cases", "single_char"],
    )
    def test_normalize_names(self, names, expected):
        assert normalize_names(names) == expected

    @pytest.mark.parametrize(
        "emails, expected",
        [
            (
                ["a@b.com", "@invalid", "good@em.com"],
                ["a@b.com", "good@em.com"],
            ),
            (["test@", "@test", "a@b"], []),
            (
                ["val@email.uk", "val2@email.ru"],
                ["val@email.uk", "val2@email.ru"],
            ),
            ([], []),
            (["a@b", "a@b@c"], []),
        ],
        ids=["mixed_valid", "all_invalid", "all_valid", "empty", "edge_cases"],
    )
    def test_remove_invalid_emails(self, emails, expected):
        assert remove_invalid_emails(emails) == expected

    @pytest.mark.parametrize(
        "words, expected",
        [
            (["Level", "Python", "Madam"], ["Level", "Madam"]),
            (["racecar", "deified", "rotor"], ["racecar", "deified", "rotor"]),
            (["hello", "world"], []),
            ([], []),
            (["a", "bb", "ccc"], ["a", "bb", "ccc"]),
        ],
        ids=[
            "mixed",
            "all_palindromes",
            "no_palindromes",
            "empty",
            "single_chars",
        ],
    )
    def test_filter_palindromes(self, words, expected):
        assert filter_palindromes(words) == expected

    @pytest.mark.parametrize(
        "n, expected",
        [
            (5, 120),
            (0, 1),
            (1, 1),
            (10, 3628800),
            (3, 6),
        ],
        ids=["normal", "zero", "one", "large", "small"],
    )
    def test_calculate_factorial(self, n, expected):
        assert calculate_factorial(n) == expected

    @pytest.mark.parametrize(
        "strings, expected",
        [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            (["interspecies", "interstellar", "interstate"], "inters"),
            ([""], ""),
            (["same", "same", "same"], "same"),
        ],
        ids=["common", "no_common", "long_prefix", "empty_string", "all_same"],
    )
    def test_find_common_prefix(self, strings, expected):
        assert find_common_prefix(strings) == expected
