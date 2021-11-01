# https://leetcode.com/problems/fibonacci-number/

class Solution:
    store = {
        0: 0,
        1: 1,
    }

    def fib(self, n: int) -> int:
        if n in self.store:
            return self.store.get(n)
        self.store[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.store.get(n)

    def fib2(self, n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':

    n = 15
    expected = 2
    print(Solution().fib(n))
