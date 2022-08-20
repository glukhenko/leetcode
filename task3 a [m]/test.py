import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "abcabcbb"
        expected = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case2(self):
        s = "bbbbb"
        expected = 1
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case3(self):
        s = "pwwkew"
        expected = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case4(self):
        s = ""
        expected = 0
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case5(self):
        s = " "
        expected = 1
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case6(self):
        s = "dvdf"
        expected = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case7(self):
        s = "tmmzuxt"
        expected = 5
        self.assertEqual(Solution().lengthOfLongestSubstring(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
