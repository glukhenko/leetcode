# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            left_depth = self.minDepth(root.left) if root.left else float('inf')
            right_depth = self.minDepth(root.right) if root.right else float('inf')
            return 1 + min(left_depth, right_depth)


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = Solution().minDepth(root)
    expected = 2
    assert result == expected, f'result: {result}, expected: {expected}'
