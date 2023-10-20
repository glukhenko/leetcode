import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 1]
        k = 3
        result = Solution().containsNearbyDuplicate(nums, k)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        nums = [1, 0, 1, 1]
        k = 1
        result = Solution().containsNearbyDuplicate(nums, k)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        nums = [1, 0, 1, 0, 1]
        k = 1
        result = Solution().containsNearbyDuplicate(nums, k)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        result = Solution().containsNearbyDuplicate(nums, k)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
