class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else:
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f'{self.key}'
            width = len(line)
            height = 1
            middle = width // 2
            print(f'no child: [{line}], {width}, {height}, {middle}')
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            return self._display_aux_left()

        # Only right child.
        if self.left is None:
            return self._display_aux_right()

        return self._display_two()

    def _display_aux_left(self):
        """Формирует отображение только левого поддерева"""
        left_lines, left_width, left_height, left_middle = self.left._display_aux()
        value = f'{self.key}'
        width = len(value)
        node_line = '{left_indent}{underscore}{value}'.format(
            left_indent=(left_middle + 1) * ' ',
            underscore=(left_width - left_middle - 1) * '_',
            value=value,
        )
        branch_line = '{left_indent}{branch_symbol}{right_indent}'.format(
            left_indent=left_middle * ' ',
            branch_symbol='/',
            right_indent=(left_width - left_middle - 1 + width) * ' ',
        )
        shifted_sub_lines = [line + width * ' ' for line in left_lines]
        _lines = [node_line, branch_line] + shifted_sub_lines
        _width = left_width + width
        _height = left_height + 2
        _middle = left_width + width // 2
        print(f'only left child [{_lines}], {_width}, {_height}, {_middle}')
        return _lines, _width, _height, _middle

    def _display_aux_right(self):
        """Формирует отображение только правого поддерева"""
        right_lines, right_width, right_height, right_middle = self.right._display_aux()
        value = f'{self.key}'
        current_width = len(value)
        node_line = '{value}{underscore}{right_indent}'.format(
            value=value,
            underscore=right_middle * '_',
            right_indent=(right_width - right_middle) * ' ',
        )
        branch_line = '{left_indent}{branch_symbol}{right_indent}'.format(
            left_indent=(current_width + right_middle) * ' ',
            branch_symbol='\\',
            right_indent=(right_width - right_middle - 1) * ' ',
        )
        shifted_sub_lines = [current_width * ' ' + line for line in right_lines]
        lines = [node_line, branch_line] + shifted_sub_lines
        width = right_width + current_width
        height = right_height + 2
        middle = current_width // 2
        print(f'only right child [{lines}], {width}, {height}, {middle}')
        return lines, width, height, middle

    def _display_two(self):
        # Two children.
        left_lines, left_width, left_height, left_middle = self.left._display_aux()
        right_lines, right_width, right_height, right_middle = self.right._display_aux()
        value = f'{self.key}'
        width = len(value)
        node_line = '{indent}{left_underscore}{value}'.format(
            indent=(left_middle + 1) * ' ',
            left_underscore=(left_width - left_middle - 1) * '_',
            value=value,
            right_underscore=right_middle * '_',
            right_indent=(right_width - right_middle) * ' ',
        )
        branch_line = '{left_indent}{left_branch}{middle_indent}{right_branch}{right_indent}'.format(
            left_indent=left_middle * ' ',
            left_branch='/',
            middle_indent=(left_width - left_middle - 1 + width + right_middle) * ' ',
            right_branch='\\',
            right_indent=(right_width - right_middle - 1) * ' ',
        )
        if left_height < right_height:
            left_lines += [left_width * ' '] * (right_height - left_height)
        elif right_height < left_height:
            right_lines += [right_width * ' '] * (left_height - right_height)
        lines = [node_line, branch_line] + \
                [f'{left_line}{width * " "}{right_line}' for left_line, right_line in zip(left_lines, right_lines)]

        _lines = lines
        _width = left_width + right_width + width
        _height = max(left_height, right_height) + 2
        _middle = left_width + width // 2
        print(f'two children [{_lines}], {_width}, {_height}, {_middle}')
        return _lines, _width, _height, _middle



data = [7, 18, 85, 39, 90, 77, 65, 79, 23, 77, 51, 67, 60, 98, 5, 85, 99, 15, 39, 45, 4, 23, 25, 64, 0, 13, 90, 24, 84, 12, 38, 86, 22, 5, 19, 64, 42, 89, 81, 5, 14, 25, 16, 48, 28, 28, 13, 90, 37, 57]
# data = [7, 18, 85, 39, 90, 77, 76, 75, 74, 73, 72, 71, 70, 69]
# data = [7, 18, 85, 39, 90, 77]

b = BstNode(50)
for value in data:
    b.insert(value)
b.display()