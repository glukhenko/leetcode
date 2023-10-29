# https://leetcode.com/problems/subtree-of-another-tree

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def is_same_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if all((root1, root2)):
            return all((
                root1.val == root2.val,
                self.is_same_trees(root1.left, root2.left),
                self.is_same_trees(root1.right, root2.right),
            ))

        return not any((root1, root2))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val:
                if self.is_same_trees(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False

if __name__ == '__main__':
    root = TreeNode(3,
                    TreeNode(4,
                             TreeNode(1),
                             TreeNode(2,
                                      TreeNode(0),
                                      None,
                                      ),
                             ),
                    TreeNode(5),
                    )
    subRoot = TreeNode(4,
                       TreeNode(1),
                       TreeNode(2),
                       )
    result = Solution().isSubtree(root, subRoot)
    expected = False
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
