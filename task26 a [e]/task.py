# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # значение в 0 индексе массива считаем сразу уникальным
        i_uniq_value = 1

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[i_uniq_value] = nums[i+1]
                i_uniq_value += 1

        return i_uniq_value


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected = 5
    result = Solution().removeDuplicates(nums)
    assert result == expected, f'bad result: {result}, expected: {expected}'
