# https://leetcode.com/problems/pascals-triangle/

from typing import List, Optional


class Solution:

    def gen_nums(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums) - 1):
            num, next_num = nums[i], nums[i + 1]
            result.append(num + next_num)
        return [1] + result + [1]

    def generate(self, numRows: int) -> List[List[int]]:
        line = [1]
        result = [line]
        for _ in range(1, numRows):
            line = self.gen_nums(line)
            result.append(line)

        return result


if __name__ == '__main__':
    numRows = 5
    result = Solution().generate(numRows)
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
