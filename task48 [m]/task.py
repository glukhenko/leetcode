# https://leetcode.com/problems/rotate-image/

from typing import List
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class Solution:

    def __get_values(self, points: List[Point]):
        return [self.matrix[p.x][p.y] for p in points]

    def __set_values(self, points: List[Point], values: List[int]):
        for p, v in zip(points, values):
            self.matrix[p.x][p.y] = v

    def rotate_layer(self, from_position: Point, to_position: Point):

        count_iter = to_position.y - from_position.y
        for y in range(count_iter):
            a, b, c, d = (
                Point(from_position.x, from_position.y + y),
                Point(from_position.x + y, to_position.y),
                Point(to_position.x, to_position.y - y),
                Point(to_position.x - y, from_position.x),
            )
            self.__set_values(
                points=[b, c, d, a],
                values=self.__get_values([a, b, c, d])
            )

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        size = len(matrix)
        count_rotate = size // 2
        start_layer, end_layer = Point(0, 0), Point(size - 1, size - 1)

        for _ in range(count_rotate):
            self.rotate_layer(start_layer, end_layer)
            start_layer = Point(start_layer.x + 1, start_layer.y + 1)
            end_layer = Point(end_layer.x - 1, end_layer.y - 1)

        return self.matrix


if __name__ == '__main__':
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    result = Solution().rotate(matrix)
    assert result == expected, f'bad result: {result}, expected: {expected}'
