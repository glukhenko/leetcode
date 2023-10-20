# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}

        for i, num in enumerate(nums):
            if num in store and i - store.get(num) <= k:
                return True
            store[num] = i
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = Solution().containsNearbyDuplicate(nums)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
