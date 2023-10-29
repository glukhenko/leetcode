import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(3),
                                 TreeNode(4),
                                 ),
                        TreeNode(2,
                                 TreeNode(4),
                                 TreeNode(3),
                                 ),
                        )
        result = Solution().isSymmetric(root)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        root = TreeNode(1,
                        TreeNode(2,
                                 None,
                                 TreeNode(3),
                                 ),
                        TreeNode(2,
                                 None,
                                 TreeNode(3),
                                 ),
                        )
        result = Solution().isSymmetric(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        root = TreeNode(2,
                        TreeNode(3,
                                 TreeNode(4),
                                 TreeNode(5),
                                 ),
                        TreeNode(3,
                                 TreeNode(5),
                                 None,
                                 ),
                        )
        result = Solution().isSymmetric(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        root = TreeNode(9,
                        TreeNode(-42,
                                 None,
                                 TreeNode(76,
                                          None,
                                          TreeNode(13),
                                          ),
                                 ),
                        TreeNode(-42,
                                 TreeNode(76,
                                          None,
                                          TreeNode(13),
                                          ),
                                 None,
                                 ),
                        )
        result = Solution().isSymmetric(root)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


'''
root =
[2,3,3,4,5,5]

Use Testcase
Output
true
Expected
false

'''

if __name__ == '__main__':
    unittest.main()
