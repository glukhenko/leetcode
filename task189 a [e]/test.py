import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(Solution().rotate(nums, k), expected,
                         f'incorrect result for nums: {nums}, k: {k} expected: {expected}')

    def test_case2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]
        self.assertEqual(Solution().rotate(nums, k), expected,
                         f'incorrect result for nums: {nums}, k: {k} expected: {expected}')


if __name__ == '__main__':
    unittest.main()
