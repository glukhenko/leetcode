# https://leetcode.com/problems/search-in-rotated-sorted-array-ii

from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Суть решения:
        Использовать принцип отсортированности последовательности.
        Но бывают случаи зацикленности: [1, 0, 1, 1, 1] в которых нельзя точно сказать что какая то из частей
        отсортирована. Идентифицировать зацикленность можно left == middle == right. В таком случаем переходим от
        бинарного к линейному и смещаем указатели left++ right--
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return True
            is_cycle = nums[left] == nums[middle] == nums[right]
            if is_cycle:
                left += 1
                right -= 1
                continue

            left_sorted = nums[left] <= nums[middle]
            if left_sorted:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return False


if __name__ == '__main__':
    nums = [3, 1]
    target = 1
    result = Solution().search(nums, target)
    expected = True
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
