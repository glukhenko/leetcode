# https://leetcode.com/problems/valid-palindrome

from typing import List, Optional


class Solution:
    def isPalindrome(self, s: str) -> bool:

        first = 0
        last = len(s) - 1

        while first < last:
            if not s[first].isalnum():
                first += 1
                continue
            if not s[last].isalnum():
                last -= 1
                continue

            if s[first].lower() == s[last].lower():
                first += 1
                last -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(s)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
