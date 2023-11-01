import unittest
from typing import List

from task import Solution, ListNode


class TestTask(unittest.TestCase):

    def test_case1(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        result = Solution().isPalindrome(head)
        expected = True
        assert result == expected, f'Bad result: {result}, but expected: {expected}'

    def test_case2(self):
        head = ListNode(1, ListNode(2))
        result = Solution().isPalindrome(head)
        expected = False
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
