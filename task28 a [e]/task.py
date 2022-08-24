# https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_n = len(needle)

        for i, char in enumerate(haystack):
            if char == needle[0] and haystack[i: i + len_n] == needle:
                return i

        return -1


if __name__ == '__main__':
    haystack = 'mississippi'
    needle = 'issip'
    expected = 4
    result = Solution().strStr(haystack, needle)
    assert result == expected, f'bad result: {result}, expected: {expected}'
