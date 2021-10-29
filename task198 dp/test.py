import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 1]
        expected = 4
        self.assertEqual(Solution().rob(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [2, 7, 9, 3, 1]
        expected = 12
        self.assertEqual(Solution().rob(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
