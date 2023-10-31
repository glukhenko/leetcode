# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Надо найти где подешевле купить а потом дороже продать
        profit = cell - buy
        """
        if len(prices) == 1:
            return 0

        max_profit = 0
        buy = prices[0]

        for price in prices[1:]:
            profit = price - buy
            max_profit = max(profit, max_profit)
            buy = min(price, buy)

        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    expected = 5
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
