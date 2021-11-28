# https://leetcode.com/problems/binary-search/

from typing import List


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(v):
    pass

class Solution:
    def firstBadVersion(self, n):
        """O(log n)"""
        left = -1
        right = n
        while right > left + 1:
            version = (left + right) // 2
            if isBadVersion(version):
                right = version
            else:
                left = version

        return right


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    expected = -1
    result = Solution().search(nums, target)
    print(f'result: {result}')
