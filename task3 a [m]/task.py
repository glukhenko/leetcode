# https://leetcode.com/problems/longest-substring-without-repeating-characters

from typing import List, Optional


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Суть решения: использовать 2 указателя
        Первый указатель - говорит где начинается подстрока
        Второй указатель - ищет дубли
        Как дубль найден, надо:
        - расчитать размер подстроки
        - переместить первый указатель, пока не удалится дубль и удалить все символы по пути
        """
        visited = set()
        slow, fast = 0, 0
        max_sub = float('-inf')

        while fast < len(s):
            if s[fast] in visited:
                # расчитаем максимум
                max_sub = max(max_sub, len(visited))
                # сместим указатель начало подстроки
                while s[fast] in visited:
                    visited.remove(s[slow])
                    slow += 1

            visited.add(s[fast])
            fast += 1

        return max(max_sub, len(visited))


if __name__ == '__main__':
    s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(s)
    expected = 3
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
