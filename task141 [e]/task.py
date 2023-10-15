# https://leetcode.com/problems/linked-list-cycle

from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next

        return False


if __name__ == '__main__':
    ...
