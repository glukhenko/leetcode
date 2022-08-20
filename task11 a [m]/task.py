# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    '''
    Идея следующая, что мы помечаем левые и правые границы, считаем площадь. Одна граница у нас будет ниже, а вторая
    ниже. Если мы будем смещать высокую границу - то новая площадь не будет больше, ибо ограничена низкой границей.
    Как следствие имеет смысл смещать низкую границу, чтобы увеличить вероятность получения более высокой плоащади.
    '''
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] > height[r]:
                local_area = height[r] * (r - l)
                r -= 1
            else:
                local_area = height[l] * (r - l)
                l += 1
            if local_area > area:
                area = local_area

        return area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49
    result = Solution().maxArea(height)
    assert result == expected, f'bad result: {result}, expected: {expected}'
