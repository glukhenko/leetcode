# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List, Optional


class Solution:

    def gen_nums(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums) - 1):
            num, next_num = nums[i], nums[i + 1]
            result.append(num + next_num)
        return [1] + result + [1]

    def getRow(self, rowIndex: int) -> List[int]:
        line = [1]
        for _ in range(rowIndex):
            line = self.gen_nums(line)
        return line


if __name__ == '__main__':
    rowIndex = 3
    result = Solution().gen_nums(rowIndex)
    expected = [1, 3, 3, 1]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
