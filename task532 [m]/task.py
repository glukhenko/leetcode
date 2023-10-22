# https://leetcode.com/problems/k-diff-pairs-in-an-array/

from typing import List
from collections import defaultdict


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        if k == 0:
            count_pairs = sum([1 for val_count in counter.values() if val_count > 1])
        else:
            count_pairs = sum([1 for num in counter.keys() if num + k in counter or num - k in counter])

        return count_pairs

    def findPairs2(self, nums: List[int], k: int) -> int:
        lower_store = {}
        upper_store = {}
        result = set()

        for num in nums:
            values = [lower_store.get(num), upper_store.get(num)]
            for value in values:
                if value is not None:
                    first, second = (num, value) if num < value else (value, num)
                    result.add((first, second))
            lower_store[num - k] = num
            upper_store[num + k] = num

        return len(result)


if __name__ == '__main__':
    nums = [3, 1, 4, 1, 5]
    k = 2
    result = Solution().findPairs(nums, k)
    expected = 2
    assert result == expected, f'Bad result: {result}, but expected: {expected}'

