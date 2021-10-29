from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            result += freq * [val]
        return result

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    expected = [2, 4, 4, 4]
    Solution().decompressRLElist(nums)
