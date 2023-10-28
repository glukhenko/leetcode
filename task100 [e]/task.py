# https://leetcode.com/problems/same-tree

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()

            if not any((node_p, node_q)):
                continue

            if all((node_p, node_q)) and node_p.val == node_q.val:
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)
                stack_q.append(node_q.left)
                stack_q.append(node_q.right)
            else:
                return False

        return not all((stack_p, stack_q))


if __name__ == '__main__':
    p = TreeNode(0,
                 TreeNode(-5),
                 None,
                 )
    q = TreeNode(0,
                 TreeNode(-8),
                 None,
                 )
    result = Solution().isSameTree(p, q)
    expected = False
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
