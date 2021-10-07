from leetcode.arrays.sorted_squares import Solution
import pytest


@pytest.mark.parametrize(
    "given,expected",
    [
        [[-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]],
        [[-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]],
        [[], []],
    ],
)
def test_sorted_squares(given, expected):
    solution = Solution()

    actual = solution.sortedSquares(given)

    assert actual == expected
