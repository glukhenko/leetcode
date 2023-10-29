import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(3,
                        TreeNode(4,
                                 TreeNode(1),
                                 TreeNode(2),
                                 ),
                        TreeNode(5),
                        )
        subRoot = TreeNode(4,
                           TreeNode(1),
                           TreeNode(2),
                           )
        result = Solution().isSubtree(root, subRoot)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(3,
                        TreeNode(4,
                                 TreeNode(1),
                                 TreeNode(2,
                                          TreeNode(0),
                                          None,
                                          ),
                                 ),
                        TreeNode(5),
                        )
        subRoot = TreeNode(4,
                           TreeNode(1),
                           TreeNode(2),
                           )
        result = Solution().isSubtree(root, subRoot)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
