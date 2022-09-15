# https://leetcode.com/problems/merge-sorted-array/submissions/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f, s, write_index = m - 1, n - 1, m + n - 1

        while s >= 0:
            if f >= 0 and nums1[f] > nums2[s]:
                nums1[write_index] = nums1[f]
                f -= 1
            else:
                nums1[write_index] = nums2[s]
                s -= 1
            write_index -= 1


if __name__ == '__main__':
    nums1, nums2 = [4, 5, 6, 0, 0, 0], [1, 2, 3]
    m, n = 3, 3
    expected = [1, 2, 3, 4, 5, 6]
    Solution().merge(nums1, m, nums2, n)
    result = nums1
    assert result == expected, f'result: {result}, expected: {expected}'
