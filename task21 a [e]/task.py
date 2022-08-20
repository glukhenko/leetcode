# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = []
        big_node = ListNode(101)

        result = current = ListNode()

        while list1 or list2:

            val1 = (list1 or big_node).val
            val2 = (list2 or big_node).val

            if val1 <= val2:
                node = ListNode(val1)
                list1 = list1.next
            else:
                node = ListNode(val2)
                list2 = list2.next
            current.next = node
            current = node

        return result.next


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    expected = "fl"
    result = Solution().longestCommonPrefix(strs)
    assert result == expected, f'bad result: {result}, expected: {expected}'
