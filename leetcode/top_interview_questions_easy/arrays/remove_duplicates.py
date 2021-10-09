from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        counter = 1
        i = 1
        prev = nums[0]

        while i < len(nums):
            if prev == nums[i]:
                nums[i] = 1000
            else:
                prev = nums[i]
                counter += 1

            i += 1

        nums.sort()
        return counter
