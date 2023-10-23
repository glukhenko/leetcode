# https://leetcode.com/problems/continuous-subarray-sum/

from typing import List


class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        store = set()
        module = 0
        prev_module = 0

        for num in nums:
            module = (module + num) % k
            if module in store:
                return True
            store.add(prev_module)
            prev_module = module
        return False


if __name__ == '__main__':
    nums = [23, 2, 6, 4, 7]
    nums = [5, 2, 1, 1, 2]
    # nums = [6,6,6,6]
    # (5 + x) % 6 = 5
    k = 6
    result = Solution().checkSubarraySum(nums, k)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
