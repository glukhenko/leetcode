# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

import operator
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        return reduce(operator.mul, digits, 1) - reduce(operator.add, digits, 0)


if __name__ == '__main__':
    n = 234
    expected = 15
    Solution().subtractProductAndSum(n)
