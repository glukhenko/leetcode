import unittest
from .task import SubrectangleQueries


class TestTask(unittest.TestCase):

    def test_case1(self):
        matrix = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
        result = [None]
        obj = SubrectangleQueries(matrix)
        for method, args in (
            (obj.getValue, [0, 2]),
            (obj.updateSubrectangle, [0, 0, 3, 2, 5]),
            (obj.getValue, [0, 2]),
            (obj.getValue, [3, 1]),
            (obj.updateSubrectangle, [3, 0, 3, 2, 10]),
            (obj.getValue, [3, 1]),
            (obj.getValue, [0, 2]),
        ):
            result.append(method(*args))
        expected = [None, 1, None, 5, 5, None, 10, 5]
        self.assertEqual(result, expected,
                         f'incorrect result for result: {result}, expected: {expected}')

    def test_case2(self):
        matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        result = [None]
        obj = SubrectangleQueries(matrix)
        for method, args in (
            (obj.getValue, [0, 0]),
            (obj.updateSubrectangle, [0, 0, 2, 2, 100]),
            (obj.getValue, [0, 0]),
            (obj.getValue, [2, 2]),
            (obj.updateSubrectangle, [1, 1, 2, 2, 20]),
            (obj.getValue, [2, 2]),
        ):
            result.append(method(*args))
        expected = [None, 1, None, 100, 100, None, 20]
        self.assertEqual(result, expected,
                         f'incorrect result for result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
