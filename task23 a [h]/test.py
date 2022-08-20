import unittest

from .task import Solution
from .task import ListNode


def compare_list_nodes(l, r):
    i = 0
    while all((l, r)):
        assert l.val == r.val, f'bad values in index: {i}, l[{i}].val: {l.val}, r[{i}].val: {r.val}]'
        l, r, i = l.next, r.next, i+1


class TestTask(unittest.TestCase):

    def compare_list_nodes(self, l, r):
        i = 0
        while all((l, r)):
            self.assertEqual(
                l.val,
                r.val,
                f'bad values in index: {i}, l[{i}].val: {l.val}, r[{i}].val: {r.val}]'
            )
            l, r, i = l.next, r.next, i + 1

    def test_case1(self):
        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        result = Solution().mergeKLists(lists)
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
        self.compare_list_nodes(result, expected)

    def test_case2(self):
        lists = []
        result = Solution().mergeKLists(lists)
        expected = []
        self.compare_list_nodes(result, expected)

    def test_case3(self):
        lists = [ListNode()]
        result = Solution().mergeKLists(lists)
        expected = []
        self.compare_list_nodes(result, expected)


if __name__ == '__main__':
    unittest.main()
