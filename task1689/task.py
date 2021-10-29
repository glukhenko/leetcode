from typing import List


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

    def minPartitionsSlow(self, n: str) -> int:
        return max(map(int, list(n)))

    def minPartitionsSlow2(self, n: str) -> int:
        max_digit = 0
        for digit in n:
            digit = int(digit)
            if digit > max_digit:
                max_digit = digit
        return max_digit


if __name__ == '__main__':
    n = "32"
    expected = 3
    Solution().minPartitions(n)
