import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        result = Solution().rotate(matrix)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        result = Solution().rotate(matrix)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[3, 1], [4, 2]]
        result = Solution().rotate(matrix)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case4(self):
        matrix = []
        expected = []
        result = Solution().rotate(matrix)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case5(self):
        matrix = [123]
        expected = [123]
        result = Solution().rotate(matrix)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
