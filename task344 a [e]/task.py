# https://leetcode.com/problems/reverse-string/submissions/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[:] = s[::-1]
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    expected = ["o", "l", "l", "e", "h"]
    result = Solution().reverseString(s)
    print(f'result: {result}')
