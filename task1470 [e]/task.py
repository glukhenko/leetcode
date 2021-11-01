# https://leetcode.com/problems/shuffle-the-array/

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [el for pair in zip(nums[:n], nums[n:]) for el in pair]

if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    expected = [2, 3, 5, 4, 1, 7]
    Solution().shuffle(nums, n)
