# https://leetcode.com/problems/palindrome-linked-list

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return '->'.join(map(str, result))


class Solution:

    def reverse_list(self, node: Optional[ListNode]) -> ListNode:
        current = ListNode(0)

        while node:
            current.val = node.val
            empty = ListNode(0)
            empty.next = current
            current = empty
            node = node.next

        return current.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_head = self.reverse_list(head)

        node = head
        reversed_node = reversed_head

        while node and reversed_node:
            if node.val != reversed_node.val:
                return False
            node = node.next
            reversed_node = reversed_node.next

        return True



if __name__ == '__main__':
    head = ListNode(1, ListNode(2))
    result = Solution().isPalindrome(head)
    expected = False
    assert result == expected, f'Bad result: {result}, but expected: {expected}'
