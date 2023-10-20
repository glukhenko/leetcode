import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 1]
        result = Solution().containsDuplicate(nums)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [1, 2, 3, 4]
        result = Solution().containsDuplicate(nums)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        result = Solution().containsDuplicate(nums)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
