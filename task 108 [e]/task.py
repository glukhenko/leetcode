# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self):
        result = [self.val]
        queue = [self]
        queue_next = []

        while queue:
            node = queue.pop(0)
            if node.left:
                result.append(node.left.val)
                queue_next.append(node.left)
            if node.right:
                result.append(node.right.val)
                queue_next.append(node.right)
            if not queue and queue_next:
                queue = queue_next[:]
                queue_next.clear()
        return result

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        center = len(nums) // 2
        left_tree = self.sortedArrayToBST(nums[:center])
        right_tree = self.sortedArrayToBST(nums[center+1:])

        return TreeNode(nums[center], left_tree, right_tree)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    result = Solution().sortedArrayToBST(nums).to_list()
    expected = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5))).to_list()
    assert result == expected, f'result: {result}, expected: {expected}'
