import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = 'Hello World'
        expected = 5
        result = Solution().lengthOfLastWord(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        s = '   fly me   to   the moon  '
        expected = 4
        result = Solution().lengthOfLastWord(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        s = 'luffy is still joyboy'
        expected = 6
        result = Solution().lengthOfLastWord(s)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
