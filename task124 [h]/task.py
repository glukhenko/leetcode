# https://leetcode.com/problems/binary-tree-maximum-path-sum

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, node: Optional[TreeNode]) -> int:
        """Возвращает для каждого узла вес с наилучшим ребенком"""
        is_leaf = (node.left, node.right) == (None, None)
        if is_leaf:
            self.max_size = max(self.max_size, node.val)
            return node.val
        # это узел
        size_left = self.dfs(node.left) if node.left else 0
        size_right = self.dfs(node.right) if node.right else 0

        size_node_with_children = size_left + node.val + size_right
        size_node_with_best_branch = node.val + max(size_left, size_right)
        self.max_size = max(self.max_size, node.val, size_node_with_children, size_node_with_best_branch)
        return max(node.val, size_node_with_best_branch)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Суть решения:
        Идя по DFS наверх мы актуализируем максимум проверя:
        - вес листа
        - вес узла:
        -- вес самого
        -- вес узла с учетом всех детей
        -- вес узла с учетом лучшей ветки
        """
        self.max_size = float('-inf')
        self.dfs(root)
        return self.max_size


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    expected = 7
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
