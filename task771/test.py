import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        jewels = "aA"
        stones = "aAAbbbb"
        expected = 3
        self.assertEqual(Solution().numJewelsInStones(jewels, stones), expected,
                         f'incorrect result for jewels: {jewels}, stones: {stones} expected: {expected}')

    def test_case2(self):
        jewels = "z"
        stones = "ZZ"
        expected = 0
        self.assertEqual(Solution().numJewelsInStones(jewels, stones), expected,
                         f'incorrect result for jewels: {jewels}, stones: {stones} expected: {expected}')

if __name__ == '__main__':
    unittest.main()
