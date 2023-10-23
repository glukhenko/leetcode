import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [23, 2, 4, 6, 7]
        k = 6
        result = Solution().checkSubarraySum(nums, k)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [23, 2, 6, 4, 7]
        k = 6
        result = Solution().checkSubarraySum(nums, k)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [23, 2, 6, 4, 7]
        k = 13
        result = Solution().checkSubarraySum(nums, k)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
