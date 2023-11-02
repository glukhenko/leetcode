import unittest
from typing import List, Optional

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        result = Solution().compress(chars)
        expected = 6
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        chars = ["a"]
        result = Solution().compress(chars)
        expected = 1
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        result = Solution().compress(chars)
        expected = 4
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
