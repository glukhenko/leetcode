import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        result = Solution().searchRange(nums, target)
        expected = [3, 4]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        result = Solution().searchRange(nums, target)
        expected = [-1, -1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = []
        target = 0
        result = Solution().searchRange(nums, target)
        expected = [-1, -1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
