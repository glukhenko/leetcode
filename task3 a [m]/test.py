import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "abcabcbb"
        result = Solution().lengthOfLongestSubstring(s)
        expected = 3
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "bbbbb"
        result = Solution().lengthOfLongestSubstring(s)
        expected = 1
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        s = "pwwkew"
        result = Solution().lengthOfLongestSubstring(s)
        expected = 3
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        s = "dvdf"
        result = Solution().lengthOfLongestSubstring(s)
        expected = 3
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
