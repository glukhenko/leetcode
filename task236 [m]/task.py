# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def get_path_node(self, node: TreeNode, target: int) -> List[int]:
        def dfs(node, path) -> bool:
            """
            Рекурсивно проходим по дереву
            - узел в детях найден - не извлекаем из стека
            - узел в детях не найден - извлекаем элемент и идем выше
            """
            if not node:
                return False
            path.append(node)

            if node.val == target:
                return True

            children_path_exists = dfs(node.left, path) or dfs(node.right, path)
            if children_path_exists:
                return True
            else:
                path.pop()
                return False

        path = []
        dfs(node, path)
        return path

    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> TreeNode:
        path_p = self.get_path_node(root, p.val)
        path_q = self.get_path_node(root, q.val)

        common_parent = None
        for node_p, node_q in zip(path_p, path_q):
            if node_p.val == node_q.val:
                common_parent = node_p
            else:
                break

        return common_parent


if __name__ == '__main__':
    root = TreeNode(3,
                    TreeNode(5,
                             TreeNode(6),
                             TreeNode(2,
                                      TreeNode(7),
                                      TreeNode(4),
                                      ),
                             ),
                    TreeNode(1,
                             TreeNode(0),
                             TreeNode(8),
                             ),
                    )
    p = TreeNode(5)
    q = TreeNode(1)
    result = Solution().lowestCommonAncestor(root, p, q)
    expected = 3
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
