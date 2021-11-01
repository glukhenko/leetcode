# https://leetcode.com/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            nums[0] + self.sub_rob(nums[2:-1]),
            self.sub_rob(nums[1:]),
        )

    @staticmethod
    def sub_rob(nums: List[int]) -> int:
        first, second = 0, 0
        for i in nums:
            first, second = second, max(first + i, second)
        return second


if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = [1, 2, 3, 1]
    nums = [1]
    expected = 1
    print(Solution().rob(nums))
