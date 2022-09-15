import unittest

from work_space.task import TreeNode, Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
        result = Solution().inorderTraversal(root)
        expected = [1, 3, 2]
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        root = None
        result = Solution().inorderTraversal(root)
        expected = []
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        root = TreeNode(1)
        result = Solution().inorderTraversal(root)
        expected = [1]
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
