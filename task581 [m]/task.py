# https://leetcode.com/problems/shortest-unsorted-continuous-subarray

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Необходимо найти границы подпоследовательности left:right, которую нужно отсортировать
        Цель: смотреть за монотонностью, если нарушается то выкидывать лишние элементы.

        Входные данные: nums = [2, 6, 4, 8, 10, 9, 15]

        Поиск left (поиск минимального индекса)
        2:  stack: [0]               values: [2]
        6:  stack: [0, 1]            values: [2, 6]
        4:  # выкинули 6 и последовательность стала отсортированной, заметим что выкинули индекс 1 (пока минимальный)
            stack: [0, 2]            values: [2, 4]
        8:  stack: [0, 2, 3]         values: [2, 4, 8]
        10: stack: [0, 2, 3, 4]      values: [2, 4, 8, 10]
        9:  # выкинули 10 и последовательность стала отсортированной, заметим что выкинули индекс 4
            stack: [0, 2, 3, 5]      values: [2, 4, 8, 9]
        15: stack: [0, 2, 3, 5, 6]   values: [2, 4, 8, 9, 15]

        Поиск right (поиск максимального индексв)
        15: stack: [6]               values: [15]
        9:  stack: [6, 5]            values: [15, 9]
        10: # выкинули 9 и последовательность стала отсортированной, заметим что выкинули индекс 5 (пока максимальный)
            stack: [6, 4]            values: [15, 10]
        8:  stack: [6, 4, 3]         values: [15, 10, 8]
        4:  stack: [6, 4, 3, 2]      values: [15, 10, 8, 4]
        6:  # выкинули 4 и последовательность стала отсортированной, заметим что выкинули индекс 2
            stack: [6, 4, 3, 1]      values: [15, 10, 8, 6]
        2:  stack: [6, 4, 3, 1, 0]   values: [15, 10, 8, 6, 2]

        Используем стек чтобы хранить индексы монотонности
        Если монотонность нарушается - то удаляем числа в стеке, до тех пор пока стек с текущим значением не сформируют
        монотонность.
        В момент когда монотонность нарушается индекс "плохого числа" это потенциальный индекс, который мы ищем.
        """
        left, right = len(nums) - 1, 0
        stack = []

        # search min left index
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack[-1])
                stack.pop()
            stack.append(i)

        stack = []
        # search max right index
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack[-1])
                stack.pop()
            stack.append(i)

        return right - left + 1 if left < right else 0


if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    result = Solution().findUnsortedSubarray(nums)
    expected = 5
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
