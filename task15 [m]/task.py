# https://leetcode.com/problems/3sum/description/

from typing import List, Set, Tuple
from collections import defaultdict


class Solution:

    def group_nums(self, nums: List[int]):
        """
        Группируем числа на positive/negative/zero
        """
        p, n, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        return p, n, z

    def zero_cases(self, n, z, p_set) -> List[List[int]]:
        result = set()
        if z:
            for num in n:
                if -num in p_set:
                    result.add((0, -num, num))
        if len(z) > 2:
            result.add((0, 0, 0))
        return result

    def two_positive_cases(self, p, n_set):
        result = set()
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in n_set:
                    result.add((p[i], p[j], target))
        return result

    def two_negative_cases(self, n, p_set):
        result = set()
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in p_set:
                    result.add((n[i], n[j], target))
        return result

    def sort_result(self, result: Set[Tuple[int]]) -> List[List[int]]:
        # уберем дубли через set
        result = set(map(lambda items: tuple(sorted(tuple(items))), result))
        result = list(map(lambda items: list(sorted(tuple(items))), result))
        result.sort()
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p, n, z = self.group_nums(nums)
        p_set, n_set = set(p), set(n)
        result = set()
        result |= self.zero_cases(n, z, p_set)
        result |= self.two_positive_cases(p, n_set)
        result |= self.two_negative_cases(n, p_set)
        return self.sort_result(result)


if __name__ == '__main__':
    nums = [1, 2, -2, -1]
    expected = []
    result = Solution().threeSum(nums)
    assert result == expected, f'bad result: {result}, expected: {expected}'
