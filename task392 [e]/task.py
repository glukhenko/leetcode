# https://leetcode.com/problems/is-subsequence

from collections import defaultdict
from typing import List, Optional


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = fast = 0

        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
                fast += 1
            else:
                fast += 1

        return slow == len(s)


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    result = Solution().isSubsequence(s, t)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
