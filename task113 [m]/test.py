import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(5,
                        TreeNode(4,
                                 TreeNode(11,
                                          TreeNode(7),
                                          TreeNode(2),
                                          ),
                                 None,
                                 ),
                        TreeNode(8,
                                 TreeNode(13),
                                 TreeNode(4,
                                          TreeNode(5),
                                          TreeNode(1),
                                          ),
                                 ),
                        )
        targetSum = 22
        result = Solution().pathSum(root, targetSum)
        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3),
                        )
        targetSum = 0
        result = Solution().pathSum(root, targetSum)
        expected = []
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = TreeNode(1,
                        TreeNode(2),
                        None,
                        )
        targetSum = 1
        result = Solution().pathSum(root, targetSum)
        expected = []
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        root = TreeNode(-2,
                        None,
                        TreeNode(-3),
                        )
        targetSum = -5
        result = Solution().pathSum(root, targetSum)
        expected = [[-2,-3]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
