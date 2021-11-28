# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:

    def isBadVersion(self, n, index):
        return n[index]

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    expected = -1
    result = Solution().search(nums, target)
    print(f'result: {result}')
