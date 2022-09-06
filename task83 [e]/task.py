# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        vals = self.to_list()
        vals = "->".join([f'[{v}]' for v in vals])
        return f'ListNode: {vals}'

    def to_list(self):
        node = copy.copy(self)
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        return vals


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head

        while current:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next

        return head

    def slow_solution(self):

        result = current = ListNode(-101)

        while head:
            if head.val != current.val:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next

        return result.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(9, ListNode(2, ListNode(3, ListNode(3)))))
    expected = ListNode(1, ListNode(2, ListNode(3)))
    result = Solution().deleteDuplicates(head)
    assert result.to_list() == expected.to_list(), f'bad result: {result}, expected: {expected}'
