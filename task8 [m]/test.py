import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "42"
        expected = 42
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        s = "   -42"
        expected = -42
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        s = "4193 with words"
        expected = 4193
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case4(self):
        s = "-2147483649"
        expected = -2147483648
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case5(self):
        s = "2147483648"
        expected = 2147483647
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case6(self):
        s = "with words"
        expected = 0
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case7(self):
        s = "words and 987"
        expected = 0
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case8(self):
        s = "-"
        expected = 0
        result = Solution().myAtoi(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
