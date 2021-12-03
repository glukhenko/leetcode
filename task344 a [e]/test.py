import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = ["h", "e", "l", "l", "o"]
        expected = ["o", "l", "l", "e", "h"]
        self.assertEqual(Solution().reverseString(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        expected = ["h", "a", "n", "n", "a", "H"]
        self.assertEqual(Solution().reverseString(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
