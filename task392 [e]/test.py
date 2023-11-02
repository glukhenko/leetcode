import unittest
from typing import List, Optional

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "abc"
        t = "ahbgdc"
        result = Solution().isSubsequence(s, t)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "axc"
        t = "ahbgdc"
        result = Solution().isSubsequence(s, t)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
