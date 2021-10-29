
class Solution:
    store = {
        1: 1,
        2: 2,
    }

    def climbStairs(self, n: int) -> int:
        if n not in self.store:
            self.store[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return self.store.get(n)

if __name__ == '__main__':

    n = 2
    expected = 2
    print(Solution().climbStairs(n))
