# https://leetcode.com/problems/merge-intervals

from typing import List, Optional


class Solution:

    def is_cross(self, i1: List[int], i2: List[int]) -> bool:
        return any((
            i2[0] <= i1[0] <= i2[1],
            i2[0] <= i1[1] <= i2[1],
            i1[0] <= i2[0] <= i1[1],
            i1[0] <= i2[1] <= i1[1],
        ))

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        current = intervals[0]

        for interval in intervals[1:]:
            if self.is_cross(current, interval):
                current = [min(current[0], interval[0]), max(current[1], interval[1])]
            else:
                result.append(current)
                current = interval

        if current not in result:
            result.append(current)

        return result


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = Solution().merge(intervals)
    expected = [[1, 6], [8, 10], [15, 18]]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
