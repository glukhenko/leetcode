# https://leetcode.com/problems/validate-binary-search-tree/

from typing import List, Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class WeightNode:
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val


class Solution:

    def dfs(self, node: TreeNode, min_val: int, max_val: int) -> bool:
        if not node:
            return True

        if min_val < node.val < max_val:
            return self.dfs(node.left, min_val, node.val) and self.dfs(node.right, node.val, max_val)
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    root = TreeNode(1)
    result = Solution().countNodes(root)
    expected = 6
    assert result == expected, f'Bad result: {result}, but expected: {expected}'

