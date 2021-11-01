import unittest
from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        boxes = "110"
        expected = [1, 1, 3]
        self.assertEqual(Solution().minOperations(boxes), expected,
                         f'incorrect result for boxes: {boxes} expected: {expected}')

    def test_case2(self):
        boxes = "001011"
        expected = [11, 8, 5, 4, 3, 4]
        self.assertEqual(Solution().minOperations(boxes), expected,
                         f'incorrect result for boxes: {boxes} expected: {expected}')


if __name__ == '__main__':
    unittest.main()
