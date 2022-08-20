# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ''

        for chars in zip(*strs):
            if len(set(chars)) > 1:
                break
            else:
                result += chars[0]

        return result


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    expected = "fl"
    result = Solution().longestCommonPrefix(strs)
    assert result == expected, f'bad result: {result}, expected: {expected}'
