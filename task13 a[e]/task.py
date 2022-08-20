# https://leetcode.com/problems/roman-to-integer/submissions/

from typing import List, Optional
from collections import defaultdict, Counter


class Solution:
    def romanToInt(self, s: str) -> int:
        ranks = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        prev, result = 0, 0

        for char in s[::-1]:
            digit = ranks[char]
            if digit < prev:
                result -= digit
            else:
                result += digit
            prev = digit

        return result


if __name__ == '__main__':
    s = "MCMXCIV"
    expected = 1994
    result = Solution().romanToInt(s)
    assert result == expected, f'bad result: {result}, expected: {expected}'
