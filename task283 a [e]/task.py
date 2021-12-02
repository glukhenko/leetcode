# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [n for n in nums if n] + [0 for n in nums if not n]


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    result = Solution().moveZeroes(nums)
    print(f'result: {result}')
