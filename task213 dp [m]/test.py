import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [2, 3, 2]
        expected = 3
        self.assertEqual(Solution().rob(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [1, 2, 3, 1]
        expected = 4
        self.assertEqual(Solution().rob(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [1, 2, 3]
        expected = 3
        self.assertEqual(Solution().rob(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case4(self):
        nums = [1]
        expected = 1
        self.assertEqual(Solution().rob(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
