# https://leetcode.com/problems/add-strings

from collections import defaultdict
from typing import List, Optional


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_num1, len_num2 = len(num1), len(num2)
        diff_length = abs(len_num1 - len_num2)

        if len_num1 < len_num2:
            num1 = '0' * diff_length + num1
        else:
            num2 = '0' * diff_length + num2

        result, over = [], 0

        for i, (digit1, digit2) in enumerate(zip(num1[::-1], num2[::-1])):
            digit = int(digit1) + int(digit2) + over
            over, remainder = divmod(digit, 10)
            result.append(remainder)
        if over:
            result.append(over)

        result = result[::-1]
        return ''.join(map(str, result))


if __name__ == '__main__':
    num1 = '11'
    num2 = '123'
    result = Solution().addStrings(num1, num2)
    expected = '134'
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
