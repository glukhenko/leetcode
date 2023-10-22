import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 2, 1]
        k = 1
        result = Solution().countKDifference(nums, k)
        expected = 4
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [1, 3]
        k = 3
        result = Solution().countKDifference(nums, k)
        expected = 0
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [3, 2, 1, 5, 4]
        k = 2
        result = Solution().countKDifference(nums, k)
        expected = 3
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
