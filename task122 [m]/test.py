import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        prices = [7, 1, 5, 3, 6, 4]
        result = Solution().maxProfit(prices)
        expected = 7
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        prices = [1, 2, 3, 4, 5]
        result = Solution().maxProfit(prices)
        expected = 4
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        prices = [7, 6, 4, 3, 1]
        result = Solution().maxProfit(prices)
        expected = 0
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
