# https://leetcode.com/problems/monotonic-array/

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        is_asc = False
        is_desc = False

        current = nums[0]
        for num in nums[1:]:
            if num > current:
                is_asc = True
            if num < current:
                is_desc = True
            current = num
            if all((is_asc, is_desc)):
                return False

        return True


if __name__ == '__main__':
    nums = [1, 2, 2, 3]
    result = Solution().isMonotonic(nums)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
