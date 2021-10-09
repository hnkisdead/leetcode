from .remove_duplicates import Solution
import pytest


@pytest.mark.parametrize(
    "input_,expected,result",
    [
        [[1, 1, 2], [1, 2, 1000], 2],
        [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4, 1000, 1000, 1000, 1000, 1000], 5],
        [[], [], 0],
    ],
)
def test_remove_duplicates(input_, expected, result):
    solution = Solution()

    actual = solution.removeDuplicates(input_)

    assert actual == result
    assert input_ == expected
