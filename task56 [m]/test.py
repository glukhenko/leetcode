import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = Solution().merge(intervals)
        expected = [[1, 6], [8, 10], [15, 18]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        intervals = [[1, 4], [4, 5]]
        result = Solution().merge(intervals)
        expected = [[1, 5]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
