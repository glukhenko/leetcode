import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
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

    def test_case2(self):
        nums = [1, 3]
        result = Solution().sortedArrayToBST(nums)
        expected = TreeNode(3,
                            TreeNode(1),
                            None,
                            )
        result = result.to_list()
        expected = expected.to_list()
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
