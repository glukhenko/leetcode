# https://leetcode.com/problems/shuffle-string/

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for char, i in zip(s, indices):
            result[i] = char
        return ''.join(result)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    expected = "leetcode"
    Solution().restoreString(s, indices)
