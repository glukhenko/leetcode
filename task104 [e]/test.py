import unittest

from work_space.task import TreeNode, Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(
            3, TreeNode(9), TreeNode(
                20, TreeNode(15), TreeNode(7)
            )
        )
        result = Solution().maxDepth(root)
        expected = 3
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        root = TreeNode(1, None, TreeNode(2))
        result = Solution().maxDepth(root)
        expected = 2
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
