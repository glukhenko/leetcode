# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        min_value = -2 ** 31
        max_value = 2 ** 31 - 1

        s = s.strip()
        if not s:
            return 0

        sign_exists = s[0] in ('+', '-')

        if sign_exists:
            sign = s[0]
            s = s[1:]
        else:
            sign = ''

        digits = []
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                break

        if not digits:
            return 0

        result = int(sign + ''.join(digits))
        result = max(result, min_value)
        result = min(result, max_value)
        return result


if __name__ == '__main__':
    s = "words and 987"
    expected = 0
    result = Solution().myAtoi(s)
    assert result == expected, f'bad result: {result}, expected: {expected}'
