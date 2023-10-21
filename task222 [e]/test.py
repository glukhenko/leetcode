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
                        TreeNode(3,
                                 TreeNode(6),
                                 )
                        )
        result = Solution().countNodes(root)
        expected = 6
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = []
        result = Solution().countNodes(root)
        expected = 0
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = TreeNode(1)
        result = Solution().countNodes(root)
        expected = 1
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(4),
                                 TreeNode(5),
                                 ),
                        TreeNode(3,
                                 TreeNode(6),
                                 TreeNode(7),
                                 )
                        )
        result = Solution().countNodes(root)
        expected = 7
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
