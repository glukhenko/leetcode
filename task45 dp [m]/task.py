# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Суть решения: мы проходим по контрольным точкам пока не достигнем конца. Очередная контрольная точка
        рассчитывается как наилучший максимальный прыжок, который может быть не только при обработке текущего значения,
        а также рассчитанный на предыдущем шаге.
        К примеру дано:
        [2, 3, 1, 1, 4] # последовательность
        [0, 1, 2, 3, 4] # индексы
        Контрольная точка будет в первом индексе, максимальный прыжок при котором на 2 индекс. Поскольку "наилучший"
        максимальный прыжок сейчас это второй индекс - зафиксируем что следующая контрольная точка будет во 2 индексе.
        При обработке второго значения, фиксируем что наилучший прыжок будет к индексу 4.
        При обработке третьего значения, попадаем на вторую контрольную точку и понимаем что максимальный прыжок
        (с учетом предыдущий) будет на 4 индекс, не смотря на то что из текущей позиции мы можем прыгунть только на 3
        позицию. Фиксируем второй прыжок и третью контрольную точку (которая в конечном итоге не будет обработана).
        """
        jumps, check_point, max_jump = 0, 0, 0

        for i in range(len(nums) - 1):
            max_jump = max(max_jump, i + nums[i])
            if i == check_point:
                jumps += 1
                check_point = max_jump
            print(f'[{i}] check_point: {check_point}, max_jump: {max_jump}')

        return jumps


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # ind= [0, 1]
    expected = 1
    print(Solution().jump(nums))
