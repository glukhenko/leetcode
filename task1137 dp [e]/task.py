# https://leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    store = {
        0: 0,
        1: 1,
        2: 1,
    }

    def tribonacci(self, n: int) -> int:
        if n in self.store:
            return self.store.get(n)
        self.store[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.store.get(n)

    def tribonacci2(self, n):
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c


if __name__ == '__main__':

    n = 4
    expected = 4
    print(Solution().tribonacci(n))
