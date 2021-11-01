import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [3, 4, 2]
        expected = 6
        self.assertEqual(Solution().deleteAndEarn(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [2, 2, 3, 3, 3, 4]
        expected = 9
        self.assertEqual(Solution().deleteAndEarn(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [1]
        expected = 1
        self.assertEqual(Solution().deleteAndEarn(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
