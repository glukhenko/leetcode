import unittest

from .task import Solution, ListNode


def checker_list_node(ln1, ln2):

    while ln1 and ln2:
        if ln1.val == ln2.val:
            ln1, ln2 = ln1.next, ln2.next
        else:
            return False
    return True


class TestTask(unittest.TestCase):

    def test_case1(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        result = Solution().mergeTwoLists(list1, list2)
        result = checker_list_node(result, expected)
        self.assertEqual(result, True, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        list1 = ListNode()
        list2 = ListNode()
        expected = ListNode()
        result = Solution().mergeTwoLists(list1, list2)
        result = checker_list_node(result, expected)
        self.assertEqual(result, True, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        list1 = ListNode()
        list2 = ListNode(0)
        expected = ListNode(0)
        result = Solution().mergeTwoLists(list1, list2)
        result = checker_list_node(result, expected)
        self.assertEqual(result, True, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
