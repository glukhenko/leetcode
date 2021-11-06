import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        self.assertEqual(Solution().maxSubArray(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [1]
        expected = 1
        self.assertEqual(Solution().maxSubArray(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [5, 4, -1, 7, 8]
        expected = 23
        self.assertEqual(Solution().maxSubArray(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [-1]
        expected = -1
        self.assertEqual(Solution().maxSubArray(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')



if __name__ == '__main__':
    unittest.main()
