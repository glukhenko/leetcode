import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 4]
        expected = [1, 3, 6, 10]
        self.assertEqual(Solution().runningSum(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [1, 1, 1, 1, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(Solution().runningSum(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [3, 1, 2, 10, 1]
        expected = [3, 4, 6, 16, 17]
        self.assertEqual(Solution().runningSum(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
