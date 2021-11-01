# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums):
        first, second = 0, 0
        for i in nums:
            first, second = second, max(first + i, second)
        return second


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    expected = 4
    print(Solution().rob(nums))
