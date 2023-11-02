# https://leetcode.com/problems/product-of-array-except-self

from typing import List, Optional


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Суть решения:
        - использовать агрегатор для накопления и проходить слева-направо справа налево
        - инициируем agg = 1 + result единицами
        Важно: аккуратно проходить массив с конца в начало
        """

        result = [1] * len(nums)

        agg = 1
        for i in range(len(nums)):
            result[i] = agg
            agg *= nums[i]

        agg = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= agg
            agg *= nums[i]

        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = Solution().productExceptSelf(nums)
    expected = [24, 12, 8, 6]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
