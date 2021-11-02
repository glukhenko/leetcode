import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [2, 3, 1, 1, 4]
        expected = True
        self.assertEqual(Solution().canJump(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [3, 2, 1, 0, 4]
        expected = False
        self.assertEqual(Solution().canJump(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case3(self):
        nums = [0]
        expected = True
        self.assertEqual(Solution().canJump(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
