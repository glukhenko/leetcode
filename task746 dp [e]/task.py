# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost):
        first, second = 0, 0
        for current in cost:
            first, second = second, current + min(first, second)
            print(f'[{current}] first: {first}, second: {second}')
        return min(first, second)


if __name__ == '__main__':
    cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))
