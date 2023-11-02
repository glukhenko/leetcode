import unittest
from typing import List, Optional

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "ABAB"
        k = 2
        result = Solution().characterReplacement(s, k)
        expected = 4
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "AABABBA"
        k = 1
        result = Solution().characterReplacement(s, k)
        expected = 4
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
