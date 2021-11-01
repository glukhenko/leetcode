import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        n = 234
        expected = 15
        self.assertEqual(Solution().subtractProductAndSum(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')

    def test_case2(self):
        n = 4421
        expected = 21
        self.assertEqual(Solution().subtractProductAndSum(n), expected,
                         f'incorrect result for n: {n}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
