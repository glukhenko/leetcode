# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        node = self
        if node is not None:
            while node.next:
                values.append(f'{node.val}')
                node = node.next
            values.append(f'{node.val}')
        return '=>'.join(values)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        middle = len(lists) // 2
        l, r = self.mergeKLists(lists[:middle]), self.mergeKLists(lists[middle:])
        return self.merge_two_list(l, r)

    def merge_two_list(self, l: ListNode, r: ListNode):
        temp = f'merge_two_list({l}, {r})'
        result = current = ListNode()

        while all((l, r)):
            if l.val < r.val:
                current.next = l
                l = l.next
            else:
                current.next = r
                r = r.next
            current = current.next
        current.next = l or r
        result = result.next
        print(f'{temp} => {result}')
        return result


def compare_list_nodes(l, r):
    i = 0
    while all((l, r)):
        assert l.val == r.val, f'bad values in index: {i}, l[{i}].val: {l.val}, r[{i}].val: {r.val}]'
        l, r, i = l.next, r.next, i+1


if __name__ == '__main__':
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
    result = Solution().mergeKLists(lists)

    compare_list_nodes(result, expected)