# https://leetcode.com/problems/middle-of-the-linked-list/submissions/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Суть решения:
        Создаем 2 указателя: медленный (1 шаг) и быстрый (2 шага)
        И как закончатся шаги у быстрого, значит медленный будет указывать на середину

        """
        fast = head
        slow = head

        while fast.next:
            if not fast.next.next:
                return slow.next
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == '__main__':
    pass
