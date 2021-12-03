import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "Let's take LeetCode contest"
        expected = "s'teL ekat edoCteeL tsetnoc"
        self.assertEqual(Solution().reverseWords(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case2(self):
        s = "God Ding"
        expected = "doG gniD"
        self.assertEqual(Solution().reverseWords(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
