# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size_nums = len(nums)
        good_index = size_nums - 1

        for i in range(size_nums - 2, -1, -1):
            reach = nums[i] + i
            if reach >= good_index:
                good_index = i

        return good_index == 0



if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    expected = True
    print(Solution().canJump(nums))
