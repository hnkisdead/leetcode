from leetcode.arrays.duplicate_zeros import Solution
import pytest


@pytest.mark.parametrize(
    "given,expected",
    [
        [[1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]],
        [[1, 1, 2, 3, 1, 4, 5, 0], [1, 1, 2, 3, 1, 4, 5, 0]],
        [[1, 2, 3], [1, 2, 3]],
        [[], []],
    ],
)
def test_duplicate_zeros(given, expected):
    solution = Solution()

    solution.duplicateZeros(given)

    assert given == expected
