# https://leetcode.com/problems/string-compression

from collections import defaultdict
from typing import List, Optional


class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        target_char = chars[0]
        counter = 1
        for char in chars[1:]:

            if char == target_char:
                counter += 1
            else:
                result.append(target_char)
                if counter > 1:
                    result += list(str(counter))
                target_char = char
                counter = 1

        result.append(target_char)
        if counter > 1:
            result += list(str(counter))

        return len(result)


if __name__ == '__main__':
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    result = Solution().compress(chars)
    expected = 6
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
