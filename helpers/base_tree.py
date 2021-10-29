class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BaseTree:
    """Базовый класс дерева, отвечающий за генерацию дерева по массиву"""

    SVG_SCALE = 50

    def __init__(self):
        self.root = None

    def generate_old(self, values, show=False):
        """
        Генерирует дерево
        :param values: список значений дерева
        :param show: отображает сгенерированное дерево в консоли
        """
        self.root = TreeNode(values.pop(0))
        queue = [self.root]

        for left_value, right_value in self.__get_pairs(values):
            current_node = queue.pop(0)
            if left_value is not None:
                current_node.left = TreeNode(left_value)
                queue.append(current_node.left)
            if right_value is not None:
                current_node.right = TreeNode(right_value)
                queue.append(current_node.right)
            if show:
                self.__show_node(current_node)

    def generate(self, values):
        """
        Генерирует дерево
        :param values: список значений дерева
        """
        self.root = TreeNode(values.pop(0))
        queue = [self.root]
        if len(values) % 2:
            values.append(None)

        while values:
            current_node = queue.pop(0)
            left_value = values.pop(0)
            right_value = values.pop(0)
            if left_value is not None:
                current_node.left = TreeNode(left_value)
                queue.append(current_node.left)
            if right_value is not None:
                current_node.right = TreeNode(right_value)
                queue.append(current_node.right)

        self.__create_diagram()

    def __create_diagram(self):
        """Создает svg файл с деревом"""
        ConsoleTree(self.root).generate()
        SvgTree(self.root).generate()

    @staticmethod
    def __get_pairs(values):
        """
        Возвращает попарно элементы списка
        :param values: список значений дерева
        :return: для values = [3,1,5] вернет [(3, 1), (5, None)]
        Примечание: дополняем значением None для нечетного списка
        """
        if len(values) % 2:
            values.append(None)
        return list(zip(values[::2], values[1::2]))


class ConsoleTree:

    def __init__(self, root):
        self.root = root

    def generate(self):
        """Генерирует диаграмму в текстовом формате для вывода в консоль"""
        nodes = self.get_nodes_by_bst()
        for node in nodes:
            self.__print_node(node)

    def get_nodes_by_bst(self):
        """Возвращает список всех узлов, через BST"""
        queue = [self.root]
        nodes = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.left is not None:
                queue.append(current_node.left)
                nodes.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
                nodes.append(current_node.right)
        return nodes

    def __print_node(self, node):
        """
        Выводит содержимое узла и его детей в формате [left_node] <= [node] => [right_node]
        :param node: узел
        """
        print('{l} <= [{v}] => {r}'.format(
            l=f'[{node.left.val}]' if node.left is not None else 'x',
            v=node.val,
            r=f'[{node.right.val}]' if node.right is not None else 'x',
        ))


class SvgTree:

    def __init__(self, root):
        self.root = root

    def generate(self):
        """Генерирует диаграму"""
        diagram = self.make_diagram()
        self.save(diagram)

    def make_diagram(self):
        """Создает диаграмму"""
        components = []
        rows_nodes = self.get_rows_nodes()

        for row in rows_nodes:
            print(f'row: {[n.val if n else None for n in row]}')

        for i, row_nodes in enumerate(rows_nodes):
            print(f'[{i}] {[n.val if n else None for n in row_nodes]}')
        count_width = len(rows_nodes) * 2 + 1
        count_height = len(rows_nodes)
        components.append(self.make_start(count_height))
        for i, row_nodes in enumerate(rows_nodes):
            centre = count_width // 2 + 1
            for node in row_nodes:
                components.append(self.make_circle(centre + i))
        '''
        [0] [6]                                     (8, 0)
        [1] [7, 8]                                  (4, 1) (10, 1)
        [2] [2, 7, 1, 3]                            (2, 2) (6, 2) (8, 2) (12, 2)
        [3] [9, None, 1, 4, None, None, None, 5]    (1, 3) (3, 3) (5, 3) (7, 3) ()
        '''
        components.append(self.make_end())

        # components = [
            # self.make_start(levels),
            # self.make_circle(3, 0, '6'),
            # self.make_circle(1, 1, '7'),
            # self.make_circle(5, 1, '8'),
            # self.make_circle(0, 2, '2'),
            # self.make_circle(2, 2, '7'),
            # self.make_circle(4, 2, '1'),
            # self.make_circle(6, 2, '3'),
            # self.make_end(),
        # ]
        return '\n'.join(components)

    def get_rows_nodes(self):
        """Восзращает список уровней с нодами через bst"""
        queue = [self.root]
        next_queue = []
        rows_nodes = [queue[:]]
        while queue:
            current_node = queue.pop(0)
            if current_node is None:
                continue
            next_queue.append(current_node.left)
            next_queue.append(current_node.right)
            if not queue:
                if not list(filter(None, next_queue[:])):
                    break
                queue, next_queue = next_queue, []
                rows_nodes.append(queue[:])
        return rows_nodes

    def make_start(self, levels):
        count_cell_x = 2 ** levels - 1
        count_cell_y = 2 ** (levels - 1) - 1
        width = count_cell_x * 2 * self.SVG_SCALE
        height = count_cell_y * 2 * self.SVG_SCALE
        return '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' \
               '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"\n' \
               '"http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n' \
               '<svg xmlns="http://www.w3.org/2000/svg"\n' \
               'xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"\n' \
               f'width="{width}px" height="{height}px">'

    def make_circle(self, position_x, position_y, title):
        """Генерирует круг"""
        circle_x = position_x * 2 * self.SVG_SCALE + self.SVG_SCALE
        circle_y = position_y * 2 * self.SVG_SCALE + self.SVG_SCALE
        circle = f'\t<circle cx="{circle_x}" cy="{circle_y}" r="{self.SVG_SCALE}"\n' \
                 '\tstroke="white" style="fill: blue; stroke: cadetblue; stroke-width: 1;"/>'
        text_x = circle_x - 10 * len(title)
        text_y = circle_y + 10
        text = f'\t<text x="{text_x}" y="{text_y}" text-anchor="left"\n' \
               f'\tfont-family="sans-serif" font-size="30">{title}</text>'
        return '\n'.join([circle, text])

    def make_end(self):
        return "</svg>\n"

    def save(self, diagram):
        file_name = '.\\tree.svg'
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(diagram)
