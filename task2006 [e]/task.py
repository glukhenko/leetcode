# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from typing import List
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        return sum(counter.get(num + k, 0) for num in nums)

if __name__ == '__main__':
    nums = [3, 1, 4, 1, 5]
    k = 2
    result = Solution().findPairs(nums, k)
    expected = 2
    assert result == expected, f'Bad result: {result}, but expected: {expected}'

