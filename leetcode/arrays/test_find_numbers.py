from .find_numbers import Solution
import pytest


@pytest.mark.parametrize(
    "input_,expected",
    [
        [[12, 345, 2, 6, 7896], 2],
        [[555, 901, 482, 1771], 1],
        [[], 0],
        [[100000], 1],
    ],
)
def test_find_numbers(input_, expected):
    solution = Solution()

    actual = solution.findNumbers(input_)

    assert actual == expected
