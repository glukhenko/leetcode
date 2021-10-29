from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stones.count(jewel) for jewel in jewels)

if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    expected = 3
    Solution().numJewelsInStones(jewels, stones)
