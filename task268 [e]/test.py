import unittest
from typing import List, Optional

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [3, 0, 1]
        result = Solution().missingNumber(nums)
        expected = 2
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [0, 1]
        result = Solution().missingNumber(nums)
        expected = 2
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        result = Solution().missingNumber(nums)
        expected = 8
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
