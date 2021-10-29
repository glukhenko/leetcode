import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        cost = [10, 15, 20]
        expected = 15
        self.assertEqual(Solution().minCostClimbingStairs(cost), expected,
                         f'incorrect result for cost: {cost}, expected: {expected}')

    def test_case2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected = 6
        self.assertEqual(Solution().minCostClimbingStairs(cost), expected,
                         f'incorrect result for cost: {cost}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
