import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "A man, a plan, a canal: Panama"
        result = Solution().isPalindrome(s)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "race a car"
        result = Solution().isPalindrome(s)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        s = " "
        result = Solution().isPalindrome(s)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        s = "0P"
        result = Solution().isPalindrome(s)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
