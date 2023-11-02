# https://leetcode.com/problems/sum-of-left-leaves

from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    sum_left = 0

    def dfs(self, node: TreeNode, is_left: bool) -> None:
        is_leaf = (node.left, node.right) == (None, None)
        if all((is_leaf, is_left)):
            self.sum_left += node.val
        if node.left:
            self.dfs(node.left, is_left=True)
        if node.right:
            self.dfs(node.right, is_left=False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, is_left=False)
        return self.sum_left


if __name__ == '__main__':
    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20,
                             TreeNode(15),
                             TreeNode(7),
                             ),
                    )
    result = Solution().sumOfLeftLeaves(root)
    expected = 24
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
