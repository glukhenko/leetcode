import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [0, 1, 2, 3, 4]
        index = [0, 1, 2, 2, 1]
        expected = [0, 4, 1, 3, 2]
        self.assertEqual(Solution().createTargetArray(nums, index), expected,
                         f'incorrect result for nums: {nums}, index: {index}, expected: {expected}')

    def test_case2(self):
        nums = [1, 2, 3, 4, 0]
        index = [0, 1, 2, 3, 0]
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(Solution().createTargetArray(nums, index), expected,
                         f'incorrect result for nums: {nums}, index: {index}, expected: {expected}')

    def test_case3(self):
        nums = [1]
        index = [0]
        expected = [1]
        self.assertEqual(Solution().createTargetArray(nums, index), expected,
                         f'incorrect result for nums: {nums}, index: {index}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
