import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "codeleet"
        indices = [4, 5, 6, 7, 0, 2, 1, 3]
        expected = "leetcode"
        self.assertEqual(Solution().restoreString(s, indices), expected,
                         f'incorrect result for num: {s}, indices: {indices}, expected: {expected}')

    def test_case2(self):
        s = "abc"
        indices = [0, 1, 2]
        expected = "abc"
        self.assertEqual(Solution().restoreString(s, indices), expected,
                         f'incorrect result for num: {s}, indices: {indices}, expected: {expected}')

    def test_case3(self):
        s = "aiohn"
        indices = [3, 1, 4, 2, 0]
        expected = "nihao"
        self.assertEqual(Solution().restoreString(s, indices), expected,
                         f'incorrect result for num: {s}, indices: {indices}, expected: {expected}')

    def test_case4(self):
        s = "aaiougrt"
        indices = [4, 0, 2, 6, 7, 3, 1, 5]
        expected = "arigatou"
        self.assertEqual(Solution().restoreString(s, indices), expected,
                         f'incorrect result for num: {s}, indices: {indices}, expected: {expected}')

    def test_case5(self):
        s = "art"
        indices = [1, 0, 2]
        expected = "rat"
        self.assertEqual(Solution().restoreString(s, indices), expected,
                         f'incorrect result for num: {s}, indices: {indices}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
