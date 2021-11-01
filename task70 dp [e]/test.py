import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        n = 2
        expected = 2
        self.assertEqual(Solution().climbStairs(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')

    def test_case2(self):
        n = 3
        expected = 3
        self.assertEqual(Solution().climbStairs(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
