from .duplicate_zeros import Solution
import pytest


@pytest.mark.parametrize(
    "input_,expected",
    [
        [[1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]],
        [[1, 1, 2, 3, 1, 4, 5, 0], [1, 1, 2, 3, 1, 4, 5, 0]],
        [[1, 2, 3], [1, 2, 3]],
        [[], []],
    ],
)
def test_duplicate_zeros(input_, expected):
    solution = Solution()

    solution.duplicateZeros(input_)

    assert input_ == expected
