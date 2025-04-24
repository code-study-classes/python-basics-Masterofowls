import pytest

from practice_package.sets import (
    count_unique_words,
    find_common_elements,
    find_shared_items,
    is_superset,
    remove_duplicates,
)


class TestSetsOperations:
    @pytest.mark.parametrize(
        "set1, set2, expected",
        [
            ({1, 2, 3}, {2, 3, 4}, {2, 3}),
            ({"a", "b"}, {"b", "c"}, {"b"}),
            (set(), {1, 2}, set()),
            ({1, 2}, set(), set()),
            ({1, 2, 3}, {1, 2, 3}, {1, 2, 3}),
        ],
        ids=["simple", "strings", "empty_first", "empty_second", "equal_sets"],
    )
    def test_find_common_elements(self, set1, set2, expected):
        result = find_common_elements(set1, set2)
        assert result == expected
        assert isinstance(result, set)

    @pytest.mark.parametrize(
        "set_a, set_b, expected",
        [
            ({1, 2, 3, 4}, {2, 3}, True),
            ({1, 2}, {3}, False),
            ({1, 2, 3}, {1, 2, 3}, True),
            ({"a", "b"}, {"a"}, True),
            (set(), set(), True),
            ({1, 2}, set(), True),
        ],
        ids=[
            "true_case",
            "false_case",
            "equal_sets",
            "strings",
            "both_empty",
            "empty_subset",
        ],
    )
    def test_is_superset(self, set_a, set_b, expected):
        assert is_superset(set_a, set_b) == expected

    @pytest.mark.parametrize(
        "items, expected",
        [
            ([3, 1, 2, 1, 4], [3, 1, 2, 4]),
            (["a", "b", "a", "c"], ["a", "b", "c"]),
            ([], []),
            ([1, 2, 3], [1, 2, 3]),
            ([1, 1, 1], [1]),
        ],
        ids=["numbers", "strings", "empty", "no_duplicates", "all_same"],
    )
    def test_remove_duplicates(self, items, expected):
        result = remove_duplicates(items)
        assert result == expected
        assert isinstance(result, list)

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("Hello hello world", 2),
            ("Python python PYTHON", 1),
            ("a b c d e", 5),
            ("", 0),
            ("word", 1),
            ("test test test", 1),
        ],
        ids=[
            "case_insensitive",
            "all_same",
            "all_unique",
            "empty",
            "single",
            "repeats",
        ],
    )
    def test_count_unique_words(self, text, expected):
        assert count_unique_words(text) == expected

    @pytest.mark.parametrize(
        "sets, expected",
        [
            (({1, 2, 3}, {2, 3, 4}, {3, 5}), {3}),
            (({"a", "b"}, {"a", "c"}), {"a"}),
            (({1, 2}, {3, 4}, {5, 6}), set()),
            (({1, 2}, {1, 2}), {1, 2}),
            ((set(), {1, 2}), set()),
            (({1}, {1}, {1}, {1}), {1}),
        ],
        ids=[
            "three_sets",
            "two_sets",
            "no_common",
            "equal_sets",
            "empty_set",
            "multiple_sets",
        ],
    )
    def test_find_shared_items(self, sets, expected):
        result = find_shared_items(*sets)
        assert result == expected
        assert isinstance(result, set)
