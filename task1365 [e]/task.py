# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List

class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """Подсчет через хэш"""
        store = {}
        for i, n in enumerate(sorted(nums)):
            if store.get(n) is None:
                store[n] = i
        return [store[n] for n in nums]

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        """Подсчет через карту"""
        store = [0] * 101
        # записываем входные числа в карту
        for num in nums:
            store[num] += 1
        # сделаем редьюс по карте
        for i in range(1, 101):
            store[i] += store[i - 1]
        # сформируем результат
        return [store[num - 1] if num else 0 for num in nums]

    def smallerNumbersThanCurrentVerySlow(self, nums: List[int]) -> List[int]:
        return [len(list(filter(lambda el: el < num, nums))) for num in nums]

if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    expected = [4, 0, 1, 1, 3]
    Solution().smallerNumbersThanCurrent(nums)
