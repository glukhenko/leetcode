# https://leetcode.com/problems/path-sum

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, expected_val = stack.pop(0)
            is_leaf = not any((node.left, node.right))
            if node.val == expected_val and is_leaf:
                return True
            if node.left:
                stack.append((node.left, expected_val - node.val))
            if node.right:
                stack.append((node.right, expected_val - node.val))

        return False



if __name__ == '__main__':
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
                                      None,
                                      TreeNode(1)
                                      ),
                             ),
                    )
    targetSum = 22
    result = Solution().hasPathSum(root, targetSum)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
