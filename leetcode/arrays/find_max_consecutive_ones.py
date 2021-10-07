from typing import List

class Solution(object):
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        counter = 0
        counters = []
        for num in nums:
            if num == 1:
                counter += 1
            if num == 0:
                counters.append(counter)
                counter = 0

        counters.append(counter)

        return sorted(counters, reverse=True)[0]