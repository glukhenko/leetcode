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
        result = Solution().zigzagLevelOrder(root)
        expected = [[3], [20, 9], [15, 7]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(1)
        result = Solution().zigzagLevelOrder(root)
        expected = [[1]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = None
        result = Solution().zigzagLevelOrder(root)
        expected = []
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
