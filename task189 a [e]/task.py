# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        border_index = - (k % len(nums))
        nums[:] = nums[border_index:] + nums[:border_index]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expected = [5, 6, 7, 1, 2, 3, 4]
    result = Solution().rotate(nums, k)
    print(f'result: {result}')
