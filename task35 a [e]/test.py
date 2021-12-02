import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        self.assertEqual(Solution().searchInsert(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')

    def test_case2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expected = 1
        self.assertEqual(Solution().searchInsert(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')

    def test_case3(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected = 4
        self.assertEqual(Solution().searchInsert(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')

    def test_case4(self):
        nums = [1, 3, 5, 6]
        target = 0
        expected = 0
        self.assertEqual(Solution().searchInsert(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')

    def test_case5(self):
        nums = [1]
        target = 0
        expected = 0
        self.assertEqual(Solution().searchInsert(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')

    def test_case6(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        expected = 2
        self.assertEqual(Solution().searchInsert(nums, target), expected,
                         f'incorrect result for nums: {nums}, target: {target}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
