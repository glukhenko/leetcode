import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 1, 1, 3]
        expected = 4
        self.assertEqual(Solution().numIdenticalPairs(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [1, 1, 1, 1]
        expected = 6
        self.assertEqual(Solution().numIdenticalPairs(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [1, 2, 3]
        expected = 0
        self.assertEqual(Solution().numIdenticalPairs(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
