from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [kid_candies + extraCandies >= max_candies for kid_candies in candies]

if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    expected = [True, True, True, False, True]
    Solution().kidsWithCandies(candies, extraCandies)
