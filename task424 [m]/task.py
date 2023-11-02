# https://leetcode.com/problems/longest-repeating-character-replacement

from collections import defaultdict
from typing import List, Optional


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        counter = defaultdict(int)
        left, right = 0, 0
        max_freq_char = 0
        longest_charset = 0

        while right < len(s):
            open_char, close_char = s[left], s[right]

            counter[close_char] += 1
            max_freq_char = max(max_freq_char, counter[close_char])

            size_window = right - left + 1
            window_valid = size_window - max_freq_char <= k

            if window_valid:
                longest_charset = max(longest_charset, size_window)
            else:
                counter[open_char] -= 1
                left += 1

            right += 1

        return longest_charset


if __name__ == '__main__':
    s = "AABABBA"
    k = 1
    result = Solution().characterReplacement(s, k)
    expected = 4
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
