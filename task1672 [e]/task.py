# https://leetcode.com/problems/richest-customer-wealth/

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(acc_customer) for acc_customer in accounts)

if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    expected = 6
    Solution().maximumWealth(accounts)
