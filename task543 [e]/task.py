# https://leetcode.com/problems/diameter-of-binary-tree

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Нужно рассчитывать диаметр для каждого узла и обновлять максимум
        """
        self.depth(root)
        return self.max_diameter

    def depth(self, node: Optional[TreeNode]) -> int:
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        if left + right > self.max_diameter:
            self.max_diameter = left + right
        return 1 + max((left, right))


if __name__ == '__main__':
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
