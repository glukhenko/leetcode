import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        result = Solution().longestCommonPrefix(strs)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        strs = ["dog", "racecar", "car"]
        expected = ""
        result = Solution().longestCommonPrefix(strs)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        strs = ["dog"]
        expected = "dog"
        result = Solution().longestCommonPrefix(strs)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case5(self):
        strs = ["cir", "car"]
        expected = "c"
        result = Solution().longestCommonPrefix(strs)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case6(self):
        strs = ["aa", "ab"]
        expected = "a"
        result = Solution().longestCommonPrefix(strs)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
