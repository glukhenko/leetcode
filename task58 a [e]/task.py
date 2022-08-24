# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        find_word = False
        counter = 0

        while i >= 0:

            if s[i] == ' ':
                if find_word:
                    return counter
            else:
                find_word = True
                counter += 1
            i -= 1

        return counter

    def lengthOfLastWord2(self, s: str) -> int:
        return len(s.strip().split()[-1])


if __name__ == '__main__':
    s = 'Hello World'
    expected = 5
    result = Solution().lengthOfLastWord(s)
    assert result == expected, f'bad result: {result}, expected: {expected}'
