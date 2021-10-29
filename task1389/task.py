from helpers.base_tree import TreeNode, BaseTree
from typing import List

class Solution:

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result

    def createTargetArraySlow(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, v in zip(index, nums):
            result.insert(i, v)
        return result

if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    expected = [0, 4, 1, 3, 2]
    print(Solution().createTargetArray(nums, index))
