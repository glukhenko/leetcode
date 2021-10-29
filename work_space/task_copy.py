from helpers.base_tree import TreeNode, BaseTree


class Solution(BaseTree):
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        next_queue = []
        result = 0
        while queue:
            current_node = queue.pop(0)
            if current_node.l is not None:
                next_queue.append(current_node.l)
            if current_node.r is not None:
                next_queue.append(current_node.r)
            result += current_node.v
            if not queue:
                if not next_queue:
                    break
                result = 0
                queue, next_queue = next_queue, []

        return result


if __name__ == '__main__':
    values = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
    expected = 19
    tree = Solution()
    tree.generate(values)
    tree.deepestLeavesSum(tree.root)
