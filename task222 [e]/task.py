# https://leetcode.com/problems/count-complete-tree-nodes

from typing import List, Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        print(f'calc countNodes({root})')
        if not root:
            return 0

        left_h = self.left_height(root)
        right_h = self.right_height(root)

        if left_h == right_h:
            return 2 ** left_h + 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def left_height(self, node: TreeNode) -> int:
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def right_height(self, node: TreeNode) -> int:
        height = 0
        while node:
            height += 1
            node = node.right
        return height


if __name__ == '__main__':
    root = TreeNode(1)
    result = Solution().countNodes(root)
    expected = 6
    assert result == expected, f'Bad result: {result}, but expected: {expected}'

