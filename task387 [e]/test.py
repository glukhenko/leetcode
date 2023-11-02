import unittest
from typing import List, Optional

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "leetcode"
        result = Solution().firstUniqChar(s)
        expected = 0
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "loveleetcode"
        result = Solution().firstUniqChar(s)
        expected = 2
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        s = "aabb"
        result = Solution().firstUniqChar(s)
        expected = -1
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
