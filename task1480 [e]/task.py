# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List
from functools import reduce

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # return self.runningSumSlow(nums)
        accumulate = 0
        result = []
        for n in nums:
            accumulate += n
            result.append(accumulate)
        return result

    def runningSumSlow(self, nums: List[int]) -> List[int]:
        return [reduce(lambda x, y: x + y, nums[:i+1]) for i in range(len(nums))]

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    expected = [1, 3, 6, 10]
    Solution().runningSum(nums)

