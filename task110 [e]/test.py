import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(3,
                        TreeNode(9),
                        TreeNode(20,
                                 TreeNode(15),
                                 TreeNode(7),
                                 ),
                        )
        result = Solution().isBalanced(root)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(2,
                                 TreeNode(3,
                                          TreeNode(4),
                                          TreeNode(4),
                                          ),
                                 TreeNode(3),
                                 ),
                        )
        result = Solution().isBalanced(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = None
        result = Solution().isBalanced(root)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        root = TreeNode(1,
                        TreeNode(2, TreeNode(3, TreeNode(4))),
                        TreeNode(2, None, TreeNode(3, None, TreeNode(4))),
                        )
        result = Solution().isBalanced(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
