# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        """O(log n)"""
        left = -1
        right = len(nums)
        while right > left + 1:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            else:
                left = middle
        if left >= 0 and nums[left] == target:
            return left
        else:
            return -1

    def search2(self, nums: List[int], target: int) -> int:
        """O(n)"""
        return nums.index(target) if target in nums else -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    expected = -1
    result = Solution().search(nums, target)
    print(f'result: {result}')
