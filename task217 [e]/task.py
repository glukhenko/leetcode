# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = set()
        for num in nums:
            if num in uniq:
                return True
            uniq.add(num)
        return False

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = Solution().containsDuplicate(nums)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
