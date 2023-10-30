import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        path = "/home/"
        result = Solution().simplifyPath(path)
        expected = "/home"
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        path = "/../"
        result = Solution().simplifyPath(path)
        expected = "/"
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        path = "/home//foo/"
        result = Solution().simplifyPath(path)
        expected = "/home/foo"
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
