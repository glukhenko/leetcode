# https://leetcode.com/problems/partition-labels/

from typing import List
from collections import defaultdict


class Solution:

    def partitionLabels(self, s: str) -> List[int]:

        all_chars = defaultdict(int)
        used_chars = set()
        reach_chars = defaultdict(int)

        result = []

        for char in s:
            all_chars[char] += 1

        index_start_sub = 0
        for i, char in enumerate(s):
            used_chars.add(char)
            reach_chars[char] += 1

            # определяет среди использованных букв used_chars, равны ли счетчики all_chars и reach_chars
            same_counts = map(lambda uc: reach_chars[uc] == all_chars[uc], used_chars)
            is_uniq_sub = all(same_counts)

            if is_uniq_sub:
                start_sub, end_sub = index_start_sub, i
                result.append(end_sub - start_sub + 1)
                used_chars.clear()
                reach_chars.clear()
                index_start_sub = i + 1

        return result


if __name__ == '__main__':
    s = "eccbbbbdec"
    result = Solution().partitionLabels(s)
    expected = [10]
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
