# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected = 5
    expected_nums = sorted([0, 1, 4, 0, 3])
    result = Solution().removeElement(nums, val)
    result_nums = sorted(nums[:result])
    assert result == expected, f'bad result: {result}, expected: {expected}'
    assert result_nums == expected_nums, f'bad result nums: {result_nums}, expected nums: {expected_nums}'

