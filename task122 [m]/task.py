# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Тут следует применить трюк: если при сравнивании двух соседних цен видно что график растет,
        т.е. цена растет - то надо совершать сделку
        PS: если цена будет расти и дальше, то я куплю в один день и продам подороже в след. день
        """
        if len(prices) == 1:
            return 0

        max_profit = 0
        yesterday_price = prices[0]

        for price in prices[1:]:
            if price > yesterday_price:
                max_profit += price - yesterday_price
            yesterday_price = price

        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    expected = 7
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
