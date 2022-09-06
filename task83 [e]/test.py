import unittest

from .task import ListNode
from .task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        head = ListNode(1, ListNode(1, ListNode(2)))
        expected = ListNode(1, ListNode(2))
        result = Solution().deleteDuplicates(head)
        self.assertEqual(result.to_list(), expected.to_list(), f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        expected = ListNode(1, ListNode(2, ListNode(3)))
        result = Solution().deleteDuplicates(head)
        self.assertEqual(result.to_list(), expected.to_list(), f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        head = ListNode()
        expected = ListNode()
        result = Solution().deleteDuplicates(head)
        self.assertEqual(result.to_list(), expected.to_list(), f'bad result: {result}, expected: {expected}')

    def test_case4(self):
        head = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
        expected = ListNode(1)
        result = Solution().deleteDuplicates(head)
        self.assertEqual(result.to_list(), expected.to_list(), f'bad result: {result}, expected: {expected}')

    def test_case5(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3))))))
        expected = ListNode(1, ListNode(2, ListNode(3)))
        result = Solution().deleteDuplicates(head)
        self.assertEqual(result.to_list(), expected.to_list(), f'bad result: {result}, expected: {expected}')

    def test_case6(self):
        head = None
        expected = None
        result = Solution().deleteDuplicates(head)
        self.assertEqual(result, expected, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
