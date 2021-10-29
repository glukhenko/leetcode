from helpers.base_tree import Node, BaseTree


class Tree(BaseTree):
    def __init__(self):
        super(Tree, self).__init__()

    def deppestLeavesSum(self, node):

        queue = [node]
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


data = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
tree = Tree()

tree.generate(data, show=True)
# res = tree.getTargetCopy(tree.root, tree.root, target)

# print(f'res: {res.v}')
