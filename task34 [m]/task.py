# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        first, last = 0, len(nums) - 1
        while first <= last:
            middle = (first + last) // 2
            if nums[middle] == target:
                result[0] = middle
                last = middle - 1
            elif nums[middle] < target:
                first = middle + 1
            else:
                last = middle - 1

        first, last = 0, len(nums) - 1
        while first <= last:
            middle = (first + last) // 2
            if nums[middle] == target:
                result[1] = middle
                first = middle + 1
            elif nums[middle] < target:
                first = middle + 1
            else:
                last = middle - 1

        return result


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = Solution().searchRange(nums, target)
    expected = [3, 4]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
