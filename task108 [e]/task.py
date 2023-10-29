# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self) -> List[Optional[int]]:
        result = []

        stack = [self]
        while stack:
            node = stack.pop(0)
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                result.append(None)

        last_index = len(result) - 1
        while last_index >= 0:
            if result[last_index] is not None:
                break
            last_index -= 1

        return result[:last_index + 1]


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Рекурсивный обход"""
        if not nums:
            return None
        middle = len(nums) // 2
        return TreeNode(
            val=nums[middle],
            left=self.sortedArrayToBST(nums[:middle]),
            right=self.sortedArrayToBST(nums[middle+1:]),
        )


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    result = Solution().sortedArrayToBST(nums)
    expected = TreeNode(0,
                        TreeNode(-3,
                                 TreeNode(-10),
                                 None,
                                 ),
                        TreeNode(9,
                                 TreeNode(5),
                                 None,
                                 ),
                        )
    result = result.to_list()
    expected = expected.to_list()
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
