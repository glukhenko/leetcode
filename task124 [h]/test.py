import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3),
                        )
        result = Solution().maxPathSum(root)
        expected = 6
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(-10,
                        TreeNode(9),
                        TreeNode(20,
                                 TreeNode(15),
                                 TreeNode(7),
                                 ),
                        )
        result = Solution().maxPathSum(root)
        expected = 42
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(3),
                                 None,
                                 ),
                        None,
                        )
        result = Solution().maxPathSum(root)
        expected = 6
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        root = TreeNode(0)
        result = Solution().maxPathSum(root)
        expected = 0
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case5(self):
        root = TreeNode(-2,
                        TreeNode(1),
                        None,
                        )
        result = Solution().maxPathSum(root)
        expected = 1
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case6(self):
        root = TreeNode(2,
                        TreeNode(-1),
                        None,
                        )
        result = Solution().maxPathSum(root)
        expected = 2
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case7(self):
        root = TreeNode(1,
                        TreeNode(-2),
                        TreeNode(3),
                        )
        result = Solution().maxPathSum(root)
        expected = 4
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case8(self):
        root = TreeNode(9,
                        TreeNode(6),
                        TreeNode(-3,
                                 TreeNode(-6),
                                 TreeNode(2,
                                          TreeNode(2,
                                                   TreeNode(-6,
                                                            TreeNode(-6),
                                                            None,
                                                            ),
                                                   TreeNode(-6),
                                                   ),
                                          None,
                                          ),
                                 ),
                        )
        result = Solution().maxPathSum(root)
        expected = 16
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
