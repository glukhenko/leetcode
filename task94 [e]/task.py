# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    result = Solution().inorderTraversal(root)
    expected = [1, 3, 2]
    assert result == expected, f'result: {result}, expected: {expected}'
