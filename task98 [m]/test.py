import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(2,
                        TreeNode(1),
                        TreeNode(3),
                        )
        result = Solution().isValidBST(root)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(5,
                        TreeNode(1),
                        TreeNode(4,
                                 TreeNode(3),
                                 TreeNode(6),
                                 ),
                        )
        result = Solution().isValidBST(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = TreeNode(2,
                        TreeNode(2),
                        TreeNode(2),
                        )
        result = Solution().isValidBST(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        root = TreeNode(5,
                        TreeNode(4),
                        TreeNode(6,
                                 TreeNode(3),
                                 TreeNode(7),
                                 ),
                        )
        result = Solution().isValidBST(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
