import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        result = Solution().maxArea(height)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        height = [1,1]
        expected = 1
        result = Solution().maxArea(height)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
