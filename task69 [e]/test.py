import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        x = 4
        expected = 2
        result = Solution().mySqrt(x)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        x = 8
        expected = 2
        result = Solution().mySqrt(x)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        x = 2
        expected = 1
        result = Solution().mySqrt(x)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case4(self):
        x = 3
        expected = 1
        result = Solution().mySqrt(x)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
