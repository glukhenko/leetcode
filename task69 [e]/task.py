# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = l + (r - l) // 2
            if m * m <= x < (m + 1) * (m + 1):
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1


if __name__ == '__main__':
    x = 4
    expected = 2
    result = Solution().mySqrt(x)
    assert result == expected, f'bad result: {result}, expected: {expected}'
