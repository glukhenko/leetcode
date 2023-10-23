# https://leetcode.com/problems/longest-palindromic-substring

from typing import List


class Solution:

    def get_palindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            palindrome1 = self.get_palindrome(s, i, i)
            palindrome2 = self.get_palindrome(s, i, i + 1)
            result = max(result, palindrome1, palindrome2, key=len)
        return result


if __name__ == '__main__':
    s = "babad"
    result = Solution().longestPalindrome(s)
    expected = "bab"
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
