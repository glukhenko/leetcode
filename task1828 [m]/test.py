import unittest
from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        points = [[1, 3], [3, 3], [5, 3], [2, 2]]
        queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        expected = [3, 2, 2]
        self.assertEqual(Solution().countPoints(points, queries), expected,
                         f'incorrect result for points: {points}, queries: {queries} expected: {expected}')

    def test_case2(self):
        points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
        expected = [2, 3, 2, 4]
        self.assertEqual(Solution().countPoints(points, queries), expected,
                         f'incorrect result for points: {points}, queries: {queries} expected: {expected}')

    def test_case3(self):
        points = [[1, 3], [3, 3], [5, 3], [2, 2]]
        queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
        expected = [3, 2, 2]
        self.assertEqual(Solution().countPoints(points, queries), expected,
                         f'incorrect result for points: {points}, queries: {queries} expected: {expected}')


if __name__ == '__main__':
    unittest.main()
