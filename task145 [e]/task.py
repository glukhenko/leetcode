# https://leetcode.com/problems/binary-tree-postorder-traversal

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        L R C
        Postorder обход означает что сначала нужно обработать LEFT поддерево, затем RIGHT поддерево, потом текущий
        Используем стек чтобы помещать туда текущий, правый, левый. И затем будем доставать справа из стека.
        Основная сложность заключается в том что текущий нужно обработать в конце и нам понадобятся отметки посещения.
        При первом извлечении узла из стека мы запускаем механизм обхода левого и правого поддерева
        При втором извлечении узла из стека мы понимаем что всех детей уже обработали (и левых и правых) и теперь можем
        обработать текущую ноду
        """
        stack = [root]
        visit = [False]
        result = []

        while stack:
            node, is_visit = stack.pop(), visit.pop()
            if node:
                if is_visit:
                    result.append(node.val)
                else:
                    # порядок обработки: L R C
                    stack.append(node)
                    visit.append(True)
                    stack.append(node.right)
                    visit.append(False)
                    stack.append(node.left)
                    visit.append(False)

        return result


if __name__ == '__main__':
    root = TreeNode(1,
                    TreeNode(4,
                             TreeNode(2),
                             None,
                             ),
                    TreeNode(3),
                    )
    result = Solution().postorderTraversal(root)
    expected = [2, 4, 3, 1]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
