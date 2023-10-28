import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(1,
                        None,
                        TreeNode(2,
                                 TreeNode(3),
                                 None,
                                 ),
                        )
        result = Solution().postorderTraversal(root)
        expected = [3, 2, 1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = None
        result = Solution().postorderTraversal(root)
        expected = []
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = TreeNode(1)
        result = Solution().postorderTraversal(root)
        expected = [1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        root = TreeNode(1,
                        TreeNode(4,
                                 TreeNode(2),
                                 None,
                                 ),
                        TreeNode(3),
                        )
        result = Solution().postorderTraversal(root)
        expected = [2, 4, 3, 1]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
