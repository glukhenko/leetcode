# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}

        for i, num in enumerate(numbers, start=1):
            pair = target - num
            if pair in pairs:
                return [pairs[pair], i]
            else:
                pairs[num] = i


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    expected = [1, 2]
    result = Solution().twoSum(numbers, target)
    print(f'result: {result}')

