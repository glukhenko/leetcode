import unittest
from typing import List, Optional

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(3,
                        TreeNode(5,
                                 TreeNode(6),
                                 TreeNode(2,
                                          TreeNode(7),
                                          TreeNode(4),
                                          ),
                                 ),
                        TreeNode(1,
                                 TreeNode(0),
                                 TreeNode(8),
                                 ),
                        )
        p = TreeNode(5)
        q = TreeNode(1)
        result = Solution().lowestCommonAncestor(root, p, q).val
        expected = TreeNode(3).val
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(3,
                        TreeNode(5,
                                 TreeNode(6),
                                 TreeNode(2,
                                          TreeNode(7),
                                          TreeNode(4),
                                          ),
                                 ),
                        TreeNode(1,
                                 TreeNode(0),
                                 TreeNode(8),
                                 ),
                        )
        p = TreeNode(5)
        q = TreeNode(4)
        result = Solution().lowestCommonAncestor(root, p, q).val
        expected = TreeNode(5).val
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = TreeNode(1,
                        TreeNode(2),
                        )
        p = TreeNode(1)
        q = TreeNode(2)
        result = Solution().lowestCommonAncestor(root, p, q).val
        expected = TreeNode(1).val
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
