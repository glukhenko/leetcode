# https://leetcode.com/problems/missing-number

from typing import List, Optional


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for num in range(len(nums) + 1):
            result += num
        for num in nums:
            result -= num
        return result


if __name__ == '__main__':
    nums = [3, 0, 1]
    result = Solution().missingNumber(nums)
    expected = 2
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
