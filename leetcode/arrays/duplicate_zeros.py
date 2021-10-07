from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        current_i = -1
        for i in range(len(arr)):
            if current_i == i:
                continue

            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                current_i = i + 1
