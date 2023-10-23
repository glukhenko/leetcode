import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "babad"
        result = Solution().longestPalindrome(s)
        expected = "bab"
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "cbbd"
        result = Solution().longestPalindrome(s)
        expected = "bb"
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()