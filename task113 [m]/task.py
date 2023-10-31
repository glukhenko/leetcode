# https://leetcode.com/problems/path-sum-ii

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Основные подходы:
        - использовать обновляемую targetSum для каждого узла
        - использовать один список путей
        -- по мере продвижения вниз значение добавляется
        -- по мере возврата наверх значение извлекается
        """

        self.result = []
        self.path = []
        if not root:
            return self.result
        self.dfs(root, targetSum)
        return self.result

    def dfs(self, node: Optional[TreeNode], expected_sum: int) -> None:
        if not node:
            return None
        is_leaf = (node.left, node.right) == (None, None)
        self.path.append(node.val)
        if node.val == expected_sum and is_leaf:
            self.result.append(self.path[:])
        else:
            new_expected_sum = expected_sum - node.val
            self.dfs(node.left, new_expected_sum)
            self.dfs(node.right, new_expected_sum)
        self.path.pop()


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
                                      TreeNode(5),
                                      TreeNode(1),
                                      ),
                             ),
                    )
    targetSum = 22
    result = Solution().pathSum(root, targetSum)
    expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
