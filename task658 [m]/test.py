import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 3
        result = Solution().findClosestElements(arr, k, x)
        expected = [1, 2, 3, 4]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = -1
        result = Solution().findClosestElements(arr, k, x)
        expected = [1, 2, 3, 4]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
