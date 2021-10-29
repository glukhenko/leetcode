from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = [range(nums.count(num)) for num in set(nums)]
        return sum(el for pair in pairs for el in pair)

if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    expected = 4
    Solution().numIdenticalPairs(nums)
