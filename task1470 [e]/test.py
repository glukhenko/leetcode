import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [2, 5, 1, 3, 4, 7]
        n = 3
        expected = [2, 3, 5, 4, 1, 7]
        self.assertEqual(Solution().shuffle(nums, n), expected,
                         f'incorrect result for nums: {nums}, n: {n} expected: {expected}')

    def test_case2(self):
        nums = [1, 2, 3, 4, 4, 3, 2, 1]
        n = 4
        expected = [1, 4, 2, 3, 3, 2, 4, 1]
        self.assertEqual(Solution().shuffle(nums, n), expected,
                         f'incorrect result for nums: {nums}, n: {n} expected: {expected}')

    def test_case3(self):
        nums = [1, 1, 2, 2]
        n = 2
        expected = [1, 2, 1, 2]
        self.assertEqual(Solution().shuffle(nums, n), expected,
                         f'incorrect result for nums: {nums}, n: {n} expected: {expected}')

if __name__ == '__main__':
    unittest.main()
