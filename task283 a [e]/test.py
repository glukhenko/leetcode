import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        self.assertEqual(Solution().moveZeroes(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [0]
        expected = [0]
        self.assertEqual(Solution().moveZeroes(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
