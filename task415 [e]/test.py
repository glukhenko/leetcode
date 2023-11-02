import unittest
from typing import List, Optional

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        num1 = '11'
        num2 = '123'
        result = Solution().addStrings(num1, num2)
        expected = '134'
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        num1 = '456'
        num2 = '77'
        result = Solution().addStrings(num1, num2)
        expected = '533'
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        num1 = '0'
        num2 = '0'
        result = Solution().addStrings(num1, num2)
        expected = '0'
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
