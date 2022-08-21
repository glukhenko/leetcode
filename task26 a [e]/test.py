import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 1, 2]
        expected = 2
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = 5
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
