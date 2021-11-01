import unittest
from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        n = "32"
        expected = 3
        self.assertEqual(Solution().minPartitions(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')

    def test_case2(self):
        n = "82734"
        expected = 8
        self.assertEqual(Solution().minPartitions(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')

    def test_case3(self):
        n = "27346209830709182346"
        expected = 9
        self.assertEqual(Solution().minPartitions(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
