# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = self.get_left(n, boxes)
        right = self.get_right(n, boxes)
        return [left[i] + right[i] for i in range(n)]

    def get_left(self, n, boxes):
        left = [0] * n
        left_count = int(boxes[0])
        for i in range(1, n):
            left[i] = left[i - 1] + left_count
            if int(boxes[i]):
                left_count += 1
        return left

    def get_right(self, n, boxes):
        right = [0] * n
        right_count = int(boxes[-1])
        for i in range(n-2, -1, -1):
            right[i] = right[i + 1] + right_count
            if int(boxes[i]):
                right_count += 1
        return right


if __name__ == '__main__':
    boxes = "110"
    expected = [1, 1, 3]
    boxes = "001011"
    expected = [11, 8, 5, 4, 3, 4]
    Solution().minOperations(boxes)

