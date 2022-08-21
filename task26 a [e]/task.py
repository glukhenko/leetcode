# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        slow, fast = 0, 1
        last_index = len(nums) - 1

        while fast <= last_index:
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow + 1] = nums[fast]
                slow += 1
                fast += 1

        return slow + 1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = 5
    result = Solution().removeDuplicates(nums)
    assert result == expected, f'bad result: {result}, expected: {expected}'
