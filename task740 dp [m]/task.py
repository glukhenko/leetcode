# https://leetcode.com/problems/delete-and-earn/

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        store = [0] * (max(nums) + 1)
        for i in nums:
            store[i] += i

        first, second = 0, 0
        for i in store:
            first, second = second, max(first + i, second)
        return second


if __name__ == '__main__':
    nums = [2, 2, 3, 3, 3, 4]
    expected = 9
    print(Solution().deleteAndEarn(nums))
