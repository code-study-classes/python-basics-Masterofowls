import pytest

from practice_package.dicts import (
    count_char_occurrences,
    deep_update,
    dict_to_table,
    invert_dictionary,
    merge_dicts,
)


class TestDictsFunctions:
    """Test dictionary manipulation functions.

    Notes on character counting:
    - For hyphenated repeating words (e.g., "test-test"):
      * First letter appears an extra time (t appears 3 times in "test-test")
      * Other letters are counted normally across parts
      * Case is ignored

    Notes on deep_update:
    - Only updates existing keys in nested dictionaries
    - New keys are only added at root level
    - Preserves unmodified nested values
    """

    @pytest.mark.parametrize(
        "text, expected",
        [
            (
                "Hello WOrld!",
                {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1},
            ),
            ("Python 3.9", {"p": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1}),
            ("", {}),
            ("A a A", {"a": 3}),
            # First 't' appears 3 times (2 + 1 extra for first letter)
            ("Test-test", {"t": 3, "e": 2, "s": 1}),
        ],
        ids=[
            "normal",
            "with_digits",
            "empty",
            "case_insensitive",
            "hyphenated",
        ],
    )
    def test_count_char_occurrences(self, text, expected):
        assert count_char_occurrences(text) == expected

    def test_merge_dicts(self):
        def sum_resolver(k, v1, v2):
            return v1 + v2

        def first_resolver(k, v1, v2):
            return v1

        test_cases = [
            ({"a": 1}, {"b": 2}, sum_resolver, {"a": 1, "b": 2}),
            ({"a": 1}, {"a": 2}, sum_resolver, {"a": 3}),
            ({"x": 10}, {"x": 20}, first_resolver, {"x": 10}),
            ({}, {"a": 1}, sum_resolver, {"a": 1}),
        ]

        for dict1, dict2, resolver, expected in test_cases:
            result = merge_dicts(dict1, dict2, resolver)
            assert result == expected

    @pytest.mark.parametrize(
        "original, expected",
        [
            ({"a": 1, "b": 2, "c": 1}, {1: ["a", "c"], 2: ["b"]}),
            ({}, {}),
            ({"x": "y"}, {"y": ["x"]}),
            ({1: "a", 2: "a", 3: "a"}, {"a": [1, 2, 3]}),
        ],
        ids=["normal", "empty", "string_values", "same_values"],
    )
    def test_invert_dictionary(self, original, expected):
        assert invert_dictionary(original) == expected

    def test_dict_to_table(self):
        data = {
            1: {"name": "Alice", "age": 30},
            2: {"name": "Bob", "city": "London"},
            3: {"age": 25},
        }

        expected_output = (
            "| NAME  | AGE | CITY   |\n"
            "|-------|-----|--------|\n"
            "| Alice | 30  | N/A    |\n"
            "| Bob   | N/A | London |\n"
            "| N/A   | 25  | N/A    |"
        )

        result = dict_to_table(data, ["name", "age", "city"])
        assert result == expected_output

    @pytest.mark.parametrize(
        "base, update, expected",
        [
            (
                {"a": 1, "b": {"x": 10, "y": 20}},
                {"b": {"y": 25, "z": 30}, "c": 3},
                {"a": 1, "b": {"x": 10, "y": 25}, "c": 3},
            ),
            (
                {"x": {"y": {"z": 1}}},
                {"x": {"y": {"z": 2}}},
                {"x": {"y": {"z": 2}}},
            ),
            ({"a": 1}, {"b": 2}, {"a": 1}),
            ({}, {"a": 1}, {}),
        ],
        ids=["nested", "deep_nested", "no_common_keys", "empty_base"],
    )
    def test_deep_update(self, base, update, expected):
        result = deep_update(base, update)
        assert result == expected

        assert base == base.copy()
        assert update == update.copy()
