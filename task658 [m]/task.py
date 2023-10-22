# https://leetcode.com/problems/find-k-closest-elements/

from typing import List
from collections import defaultdict


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        first, last = 0, len(arr) - k
        while first < last:
            mid = (first + last) // 2
            first_distance = x - arr[mid]
            last_k_distance = arr[mid + k] - x
            if first_distance > last_k_distance:
                first = mid + 1
            else:
                last = mid
        return arr[first:first + k]


if __name__ == '__main__':
    arr = [-8, -7, -6, -5, -4, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    # arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    result = Solution().findClosestElements(arr, k, x)
    expected = [1, 2, 3, 4]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
