import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        accounts = [[1, 2, 3], [3, 2, 1]]
        expected = 6
        self.assertEqual(Solution().maximumWealth(accounts), expected,
                         f'incorrect result for accounts: {accounts}, expected: {expected}')

    def test_case2(self):
        accounts = [[1, 5], [7, 3], [3, 5]]
        expected = 10
        self.assertEqual(Solution().maximumWealth(accounts), expected,
                         f'incorrect result for accounts: {accounts}, expected: {expected}')

    def test_case3(self):
        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        expected = 17
        self.assertEqual(Solution().maximumWealth(accounts), expected,
                         f'incorrect result for accounts: {accounts}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
