import unittest
from typing import List, Optional

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "cbaebabacd"
        p = "abc"
        result = Solution().findAnagrams(s, p)
        expected = [0, 6]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "abab"
        p = "ab"
        result = Solution().findAnagrams(s, p)
        expected = [0, 1, 2]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        s = "aaaaaaaaaa"
        p = "aaaaaaaaaaaaa"
        result = Solution().findAnagrams(s, p)
        expected = []
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
