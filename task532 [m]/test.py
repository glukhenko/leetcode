import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [3, 1, 4, 1, 5]
        k = 2
        result = Solution().findPairs(nums, k)
        expected = 2
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        result = Solution().findPairs(nums, k)
        expected = 4
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [1, 3, 1, 5, 4]
        k = 0
        result = Solution().findPairs(nums, k)
        expected = 1
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        nums = [6, 3, 5, 7, 2, 3, 3, 8, 2, 4]
        k = 2
        result = Solution().findPairs(nums, k)
        expected = 5
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case5(self):
        nums = [0, 0, 0]
        k = 0
        result = Solution().findPairs(nums, k)
        expected = 1
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
