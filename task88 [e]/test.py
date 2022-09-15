import unittest

from work_space.task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
        m, n = 3, 3
        expected = [1, 2, 2, 3, 5, 6]
        Solution().merge(nums1, m, nums2, n)
        result = nums1
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        nums1, nums2 = [1], []
        m, n = 1, 0
        expected = [1]
        Solution().merge(nums1, m, nums2, n)
        result = nums1
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        nums1, nums2 = [0], [1]
        m, n = 0, 1
        expected = [1]
        Solution().merge(nums1, m, nums2, n)
        result = nums1
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case4(self):
        nums1, nums2 = [1, 2, 3], []
        m, n = 3, 0
        expected = [1, 2, 3]
        Solution().merge(nums1, m, nums2, n)
        result = nums1
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case5(self):
        nums1, nums2 = [4, 5, 6, 0, 0, 0], [1, 2, 3]
        m, n = 3, 3
        expected = [1, 2, 3, 4, 5, 6]
        Solution().merge(nums1, m, nums2, n)
        result = nums1
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case6(self):
        nums1, nums2 = [1, 2, 4, 5, 6, 0], [3]
        m, n = 5, 1
        expected = [1, 2, 3, 4, 5, 6]
        Solution().merge(nums1, m, nums2, n)
        result = nums1
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
