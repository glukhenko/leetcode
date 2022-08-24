import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        haystack = 'hello'
        needle = 'll'
        expected = 2
        result = Solution().strStr(haystack, needle)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        haystack = 'aaaaa'
        needle = 'bba'
        expected = -1
        result = Solution().strStr(haystack, needle)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        haystack = 'aaa'
        needle = 'aaaa'
        expected = -1
        result = Solution().strStr(haystack, needle)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case4(self):
        haystack = 'mississippi'
        needle = 'issip'
        expected = 4
        result = Solution().strStr(haystack, needle)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
