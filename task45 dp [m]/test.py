import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [2, 3, 1, 1, 4]
        expected = 2
        self.assertEqual(Solution().jump(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [2, 3, 0, 1, 4]
        expected = 2
        self.assertEqual(Solution().jump(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [1, 4]
        expected = 1
        self.assertEqual(Solution().jump(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
