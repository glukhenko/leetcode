import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        n = 3
        result = Solution().generateParenthesis(n)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        n = 1
        result = Solution().generateParenthesis(n)
        expected = ["()"]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
