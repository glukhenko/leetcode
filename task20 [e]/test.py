import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "()"
        expected = True
        self.assertEqual(Solution().isValid(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case2(self):
        s = "()[]{}"
        expected = True
        self.assertEqual(Solution().isValid(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case3(self):
        s = "(]"
        expected = False
        self.assertEqual(Solution().isValid(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case4(self):
        s = "))))"
        expected = False
        self.assertEqual(Solution().isValid(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case5(self):
        s = "({[([])]})"
        expected = True
        self.assertEqual(Solution().isValid(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')

    def test_case6(self):
        s = "({[([])]}])"
        expected = False
        self.assertEqual(Solution().isValid(s), expected,
                         f'incorrect result for s: {s}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
