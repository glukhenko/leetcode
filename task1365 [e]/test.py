import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [8, 1, 2, 2, 3]
        expected = [4, 0, 1, 1, 3]
        self.assertEqual(Solution().smallerNumbersThanCurrent(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [6, 5, 4, 8]
        expected = [2, 1, 0, 3]
        self.assertEqual(Solution().smallerNumbersThanCurrent(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [7, 7, 7, 7]
        expected = [0, 0, 0, 0]
        self.assertEqual(Solution().smallerNumbersThanCurrent(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
