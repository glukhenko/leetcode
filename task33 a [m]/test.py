import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        result = Solution().search(nums, target)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        nums = [1]
        target = 0
        expected = -1
        result = Solution().search(nums, target)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
