import unittest

from work_space.task import TreeNode, Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        nums = [-10, -3, 0, 5, 9]
        result = Solution().sortedArrayToBST(nums).to_list()
        expected = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5))).to_list()
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        nums = [1, 3]
        result = Solution().sortedArrayToBST(nums).to_list()
        expected = TreeNode(3, TreeNode(1)).to_list()
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
