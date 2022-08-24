import unittest

from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected = 2
        expected_nums = sorted([2, 2])
        result = Solution().removeElement(nums, val)
        result_nums = sorted(nums[:result])
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')
        self.assertEqual(result_nums, expected_nums, f'bad result nums: {result_nums}, expected nums: {expected_nums}')

    def test_case2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = 5
        expected_nums = sorted([0, 1, 4, 0, 3])
        result = Solution().removeElement(nums, val)
        result_nums = sorted(nums[:result])
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')
        self.assertEqual(result_nums, expected_nums, f'bad result nums: {result_nums}, expected nums: {expected_nums}')

'''
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave
'''




if __name__ == '__main__':
    unittest.main()
