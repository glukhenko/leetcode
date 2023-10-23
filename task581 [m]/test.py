import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [2, 6, 4, 8, 10, 9, 15]
        result = Solution().findUnsortedSubarray(nums)
        expected = 5
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [1, 2, 3, 4]
        result = Solution().findUnsortedSubarray(nums)
        expected = 0
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [1]
        result = Solution().findUnsortedSubarray(nums)
        expected = 0
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
