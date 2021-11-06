# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Суть решения:
        Предполагаем что есть N количество субпоследовательностей. Подсчитывая сумму каждой субпоследовательности
        фиксируем наилучшую в answer.
        PS: если сумма текущей последовательности стала отрицательной, не учитываем ее, потому что с отрицательными
        суммами будет сложно набрать максимальную субпоследовательность.
        """
        answer, agg = float('-inf'), 0

        for num in nums:
            agg += num
            answer = max(agg, answer)
            if agg < 0:
                agg = 0
        return answer


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 1
    print(Solution().maxSubArray(nums))
