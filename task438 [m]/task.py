# https://leetcode.com/problems/find-all-anagrams-in-a-string

from collections import defaultdict
from typing import List, Optional


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Принципиальное решение - использовать окно и проверять счетчики двух последовательностей равной длины
        Исключим индексы если p больше s

        Основной алгоритм:
        1. Подсчитаем счетчики p и первые s символов == len(p)
        2. Если счетчики равны то определим 0 индекс
        3. В цикле пройдемся от len(p) до len(s)
        4. В итерации инкремент right символа и декремент left символа
        Важно:
        - не забыть сдвинуть left дальше
        - очистить char в счетчике s, если количество == 0
        5. Проверяем равны ли счетчики, если да, то мы нашли анаграму

        s = "cbaebabacd"
        p = "abc"
        ----------------
              v v
        s = "___ebabacd"
        p = "abc"
        '''
        if len(p) > len(s):
            return []

        counter_p = defaultdict(int)
        counter_s = defaultdict(int)

        for i in range(len(p)):
            counter_p[p[i]] += 1
            counter_s[s[i]] += 1

        left_window = 0
        result = [0] if counter_p == counter_s else []

        for right_window in range(len(p), len(s)):
            char_left_window, char_right_window = s[left_window], s[right_window]
            counter_s[char_right_window] += 1
            counter_s[char_left_window] -= 1

            if counter_s[char_left_window] == 0:
                counter_s.pop(char_left_window)

            left_window += 1

            if counter_p == counter_s:
                result.append(left_window)

        return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    result = Solution().findAnagrams(s, p)
    expected = [0, 6]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
