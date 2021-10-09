from .find_max_consecutive_ones import Solution
import pytest


@pytest.mark.parametrize(
    "input_,expected",
    [
        [[1, 1, 0, 1, 1, 1], 3],
        [[1, 0, 1, 1, 0, 1], 2],
        [[], 0],
    ],
)
def test_find_max_consecutive_ones(input_, expected):
    solution = Solution()

    actual = solution.findMaxConsecutiveOnes(input_)

    assert actual == expected
