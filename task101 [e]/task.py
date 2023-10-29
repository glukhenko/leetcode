# https://leetcode.com/problems/binary-tree-inorder-traversal

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Без рекурсии"""
        if not root:
            return True

        stack1 = [root.left]
        stack2 = [root.right]

        while all((stack1, stack2)):
            node1 = stack1.pop(0)
            node2 = stack2.pop(0)

            if all((node1, node2)):
                if node1.val != node2.val:
                    return False
                stack1.append(node1.left)
                stack1.append(node1.right)
                stack2.append(node2.right)
                stack2.append(node2.left)
            elif any((node1, node2)):
                return False

        return not any((stack1, stack2))

    def dfs(self, node1: Optional[TreeNode], node2: Optional[TreeNode]):
        if all((node1, node2)):
            return all((
                node1.val == node2.val,
                self.dfs(node1.left, node2.right),
                self.dfs(node1.right, node2.left),
            ))
        return not any((node1, node2))

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        """С рекурсией"""
        if not root:
            return True

        return self.dfs(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(9,
                    TreeNode(-42,
                             None,
                             TreeNode(76,
                                      None,
                                      TreeNode(13),
                                      ),
                             ),
                    TreeNode(-42,
                             TreeNode(76,
                                      None,
                                      TreeNode(13),
                                      ),
                             None,
                             ),
                    )
    result = Solution().isSymmetric(root)
    expected = False
    assert result == expected, f'Bad result: {result}, but expected: {expected}'