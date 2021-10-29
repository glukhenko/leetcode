import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        num = 14
        expected = 6
        self.assertEqual(Solution().numberOfSteps(num), expected,
                         f'incorrect result for num: {num}, expected: {expected}')

    def test_case2(self):
        num = 8
        expected = 4
        self.assertEqual(Solution().numberOfSteps(num), expected,
                         f'incorrect result for num: {num}, expected: {expected}')

    def test_case3(self):
        num = 123
        expected = 12
        self.assertEqual(Solution().numberOfSteps(num), expected,
                         f'incorrect result for num: {num}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
