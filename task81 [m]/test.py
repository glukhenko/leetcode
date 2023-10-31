import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 0
        result = Solution().search(nums, target)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 3
        result = Solution().search(nums, target)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [1, 0, 1, 1, 1]
        target = 0
        result = Solution().search(nums, target)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 13
        result = Solution().search(nums, target)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case5(self):
        nums = [3, 1]
        target = 1
        result = Solution().search(nums, target)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
