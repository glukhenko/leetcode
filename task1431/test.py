import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        expected = [True, True, True, False, True]
        self.assertEqual(Solution().kidsWithCandies(candies, extraCandies), expected,
                         f'incorrect result for candies: {candies}, extraCandies: {extraCandies}, expected: {expected}')

    def test_case2(self):
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        expected = [True, False, False, False, False]
        self.assertEqual(Solution().kidsWithCandies(candies, extraCandies), expected,
                         f'incorrect result for candies: {candies}, extraCandies: {extraCandies}, expected: {expected}')

    def test_case3(self):
        candies = [12, 1, 12]
        extraCandies = 10
        expected = [True, False, True]
        self.assertEqual(Solution().kidsWithCandies(candies, extraCandies), expected,
                         f'incorrect result for candies: {candies}, extraCandies: {extraCandies}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
