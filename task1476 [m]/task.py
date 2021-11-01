# https://leetcode.com/problems/subrectangle-queries/

from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        print(f'updateSubrectangle row1: {row1}, col1: {col1}, row2: {row2}, col2: {col2}, newValue: {newValue}')
        print(f'B matrix:\n {self.show()}')
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.matrix[row][col] = newValue
        print(f'A matrix:\n {self.show()}')

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def show(self):
        res = ''
        for row in self.matrix:
            res += f'{row}\n'
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
    result = [None]
    obj = SubrectangleQueries(matrix)
    for method, args in (
            (obj.getValue, [0, 2]),
            (obj.updateSubrectangle, [0, 0, 3, 2, 5]),
            (obj.getValue, [0, 2]),
            (obj.getValue, [3, 1]),
            (obj.updateSubrectangle, [3, 0, 3, 2, 10]),
            (obj.getValue, [3, 1]),
            (obj.getValue, [0, 2]),
    ):
        result.append(method(*args))
    expected = [None, 1, None, 5, 5, None, 10, 5]
    print(f'incorrect result for result: {result}, expected: {expected}')
