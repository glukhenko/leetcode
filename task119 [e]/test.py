import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        rowIndex = 3
        result = Solution().getRow(rowIndex)
        expected = [1, 3, 3, 1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        rowIndex = 0
        result = Solution().getRow(rowIndex)
        expected = [1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        rowIndex = 1
        result = Solution().getRow(rowIndex)
        expected = [1, 1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
