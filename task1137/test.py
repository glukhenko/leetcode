import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        n = 4
        expected = 4
        self.assertEqual(Solution().tribonacci(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')

    def test_case2(self):
        n = 25
        expected = 1389537
        self.assertEqual(Solution().tribonacci(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
