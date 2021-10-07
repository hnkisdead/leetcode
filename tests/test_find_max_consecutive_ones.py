from leetcode.arrays.find_max_consecutive_ones import Solution
import pytest


@pytest.mark.parametrize(
    "given,expected",
    [
        [[1, 1, 0, 1, 1, 1], 3],
        [[1, 0, 1, 1, 0, 1], 2],
        [[], 0],
    ],
)
def test_find_max_consecutive_ones(given, expected):
    solution = Solution()

    actual = solution.findMaxConsecutiveOnes(given)

    assert actual == expected
