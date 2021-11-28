import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        expected = 4
        self.assertEqual(Solution().search(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')

    def test_case2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        expected = -1
        self.assertEqual(Solution().search(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
