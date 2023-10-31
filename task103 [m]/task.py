# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        children = []
        result = []
        values_level = []
        level = 1

        while stack:
            node = stack.pop(0)
            values_level.append(node.val)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)

            if not stack:
                # обработать результат
                values = values_level if level % 2 else values_level[::-1]
                result.append(values)
                # обновить стек
                if children:
                    stack = children[:]
                    values_level = []
                    children = []

                level += 1

        return result

if __name__ == '__main__':
    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20,
                             TreeNode(15),
                             TreeNode(7),
                             ),
                    )
    result = Solution().zigzagLevelOrder(root)
    expected = [[3], [20, 9], [15, 7]]
    assert result == expected, f'Bad result: {result}_{type(result)}, but expected: {expected}_{type(expected)}'
