# https://leetcode.com/problems/first-unique-character-in-a-string

from collections import defaultdict
from typing import List, Optional


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1

        for i, char in enumerate(s):
            if counter[char] == 1:
                return i

        return -1


if __name__ == '__main__':
    s = "leetcode"
    result = Solution().firstUniqChar(s)
    expected = 0
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
