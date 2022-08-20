import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "III"
        expected = 3
        result = Solution().romanToInt(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        s = "LVIII"
        expected = 58
        result = Solution().romanToInt(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        s = "MCMXCIV"
        expected = 1994
        result = Solution().romanToInt(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
