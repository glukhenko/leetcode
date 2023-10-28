# https://leetcode.com/problems/balanced-binary-tree

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Надо проверить сбалансированы ли:
        - текущий узел
        - левый ребенок
        - правый ребенок
        """
        if not root:
            return True
        node_balance = abs(self.get_height(root.left) - self.get_height(root.right)) < 2
        return node_balance and self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))


if __name__ == '__main__':
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
