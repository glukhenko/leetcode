import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        self.assertEqual(Solution().sortedSquares(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [-7, -3, 2, 3, 11]
        expected = [4, 9, 9, 49, 121]
        self.assertEqual(Solution().sortedSquares(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
