# https://leetcode.com/problems/simplify-path

from typing import List, Optional


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/')

        stack = []
        for sub in path.split('/'):
            if sub in ('', '.', '..'):
                if sub == '..' and stack:
                    stack.pop()
            else:
                stack.append(sub)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    path = "/home/"
    result = Solution().simplifyPath(path)
    expected = "/home"
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
