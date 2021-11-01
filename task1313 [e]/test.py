import unittest
from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 2, 3, 4]
        expected = [2, 4, 4, 4]
        self.assertEqual(Solution().decompressRLElist(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')

    def test_case2(self):
        nums = [1, 1, 2, 3]
        expected = [1, 3, 3]
        self.assertEqual(Solution().decompressRLElist(nums), expected,
                         f'incorrect result for nums: {nums}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
