# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return result


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(s)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
