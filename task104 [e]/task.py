# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # if root.left is None and root.right is None:
        #     return 1
        # else:
        #     left_depth = self.maxDepth(root.left) if root.left else 0
        #     right_depth = self.maxDepth(root.right) if root.right else 0
        #     return 1 + max(left_depth, right_depth)


if __name__ == '__main__':
    root = TreeNode(
        3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)
        )
    )
    result = Solution().maxDepth(root)
    expected = 3
    assert result == expected, f'result: {result}, expected: {expected}'
