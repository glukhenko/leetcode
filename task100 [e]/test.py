import unittest
from typing import List

from task import Solution, TreeNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        p = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3),
                        )
        q = TreeNode(1,
                     TreeNode(2),
                     TreeNode(3),
                     )
        result = Solution().isSameTree(p, q)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        p = TreeNode(1,
                     TreeNode(2),
                     None,
                    )
        q = TreeNode(1,
                     None,
                     TreeNode(2),
                     )
        result = Solution().isSameTree(p, q)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        p = TreeNode(1,
                     TreeNode(2),
                     TreeNode(1),
                     )
        q = TreeNode(1,
                     TreeNode(1),
                     TreeNode(2),
                     )
        result = Solution().isSameTree(p, q)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case4(self):
        p = TreeNode(0,
                     TreeNode(-5),
                     None,
                     )
        q = TreeNode(0,
                     TreeNode(-8),
                     None,
                     )
        result = Solution().isSameTree(p, q)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
