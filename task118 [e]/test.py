import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        numRows = 5
        result = Solution().generate(numRows)
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        numRows = 1
        result = Solution().generate(numRows)
        expected = [[1]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
