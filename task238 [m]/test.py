import unittest
from typing import List, Optional

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 4]
        result = Solution().productExceptSelf(nums)
        expected = [24, 12, 8, 6]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [-1, 1, 0, -3, 3]
        result = Solution().productExceptSelf(nums)
        expected = [0, 0, 9, 0, 0]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
