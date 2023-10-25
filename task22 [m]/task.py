# https://leetcode.com/problems/generate-parentheses

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Суть решения:
        Через рекурсионный DFS мы последовательно добавляем скобки слева потом скобки справа
        Условие выхода: длина собранной строки 2n
        Левых скобок добавлем не более n
        Правых скобок добавляем не более количества левых на данной этапе рекурсии
        """
        def dfs(left: int, right: int, s: str):
            if len(s) == 2 * n:
                result.append(s)
                return None

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        result = []
        dfs(0, 0, '')
        return result


if __name__ == '__main__':
    n = 3
    result = Solution().generateParenthesis(n)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
