# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            print(f'l: {l}, r: {r}, middle: {middle}')

            if target == nums[middle]:
                return middle

            is_left_asc = nums[l] <= nums[middle]

            if is_left_asc:
                if nums[l] <= target <= nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if nums[middle] <= target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    expected = -1
    result = Solution().search(nums, target)
    assert result == expected, f'bad result: {result}, expected: {expected}'
