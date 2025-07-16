from typing import List, Optional

# Time : Beats 100.0 %
# Memo : Beats 44.26 %

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        node = head
        val = 0
        while node != None:
            val <<= 1
            val += node.val
            node = node.next
        return val