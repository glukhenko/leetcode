import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(4),
                                 TreeNode(5),
                                 ),
                        TreeNode(3),
                        )
        result = Solution().diameterOfBinaryTree(root)
        expected = 3
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(4,
                        TreeNode(-7),
                        TreeNode(-3,
                                 TreeNode(-9,
                                          TreeNode(9,
                                                   TreeNode(6,
                                                            TreeNode(0,
                                                                     None,
                                                                     TreeNode(-1)),
                                                            TreeNode(6,
                                                                     TreeNode(-4),
                                                                     None
                                                                     ),
                                                            ),
                                                   None,
                                                   ),
                                          TreeNode(-7,
                                                   TreeNode(-6,
                                                            TreeNode(5),
                                                            None,
                                                            ),
                                                   TreeNode(-6,
                                                            TreeNode(9,
                                                                     TreeNode(-2),
                                                                     None
                                                                     ),
                                                            None
                                                            ),
                                                   ),
                                          ),
                                 TreeNode(-3,
                                          TreeNode(-4),
                                          None
                                          ),
                                 ),
                        )
        result = Solution().diameterOfBinaryTree(root)
        expected = 8
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
