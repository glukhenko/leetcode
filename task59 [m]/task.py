# https://leetcode.com/problems/spiral-matrix-ii

from typing import List, Optional


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution:
    directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
    direction = 0

    def get_next_coords(self, row: int, col: int) -> (int, int):
        shift_row, shift_col = self.directions[self.direction]
        return row + shift_row, col + shift_col

    def change_direction(self):
        self.direction = (self.direction + 1) % 4

    def get_next_round_coords(self, row: int, col: int) -> (int, int):
        new_row, new_col = self.get_next_coords(row, col)
        if self.border_in_limit(new_row, new_col) and self.coords_is_empty(new_row, new_col):
            return new_row, new_col
        else:
            self.change_direction()
            new_row, new_col = self.get_next_coords(row, col)
            if self.border_in_limit(new_row, new_col) and self.coords_is_empty(new_row, new_col):
                return new_row, new_col
        return None, None

    def border_in_limit(self, row: int, col: int) -> bool:
        try:
            self.result[row][col]
        except IndexError:
            return False
        return True

    def coords_is_empty(self, row: int, col: int) -> bool:
        return not self.result[row][col]

    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Основная идея: определить направления для j++ i++ j-- i--
        Определить метод который будет возвращать round координаты и заполнять числом пока новые коррдинаты существуют
        """
        self.result = [[0] * n for _ in range(n)]
        row = col = 0
        current_number = 1

        while True:
            self.result[row][col] = current_number
            current_number += 1
            row, col = self.get_next_round_coords(row, col)
            if None in (row, col):
                break

        return self.result


if __name__ == '__main__':
    n = 3
    result = Solution().generateMatrix(n)
    expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
