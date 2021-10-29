from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for x_circle, y_circle, radius in queries:
            cross_points = 0
            for x_point, y_point in points:
                if self.point_in_circle(x_point, y_point, x_circle, y_circle, radius):
                    cross_points += 1
            result.append(cross_points)
        return result

    def point_in_circle(self, x_point, y_point, x_circle, y_circle, radius):
        """Проверяет, входит ли точка в круг"""
        return (x_point - x_circle) * (x_point - x_circle) + (y_point - y_circle) * (y_point - y_circle) <= radius ** 2



if __name__ == '__main__':
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    expected = [3, 2, 2]
    Solution().countPoints(points, queries)
