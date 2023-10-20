import unittest

# from .task import Solution
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        s = "ababcbacadefegdehijhklij"
        result = Solution().partitionLabels(s)
        expected = [9, 7, 8]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        s = "eccbbbbdec"
        result = Solution().partitionLabels(s)
        expected = [10]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case3(self):
        s = "abababcc"
        result = Solution().partitionLabels(s)
        expected = [6, 2]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

if __name__ == '__main__':
    unittest.main()
