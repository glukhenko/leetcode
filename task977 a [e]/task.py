# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = list(map(lambda x: x**2, nums))
        nums.sort()
        return nums


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    expected = [0, 1, 9, 16, 100]
    result = Solution().sortedSquares(nums)
    print(f'result: {result}')
