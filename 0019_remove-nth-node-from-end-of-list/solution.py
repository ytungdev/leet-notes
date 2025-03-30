from typing import Optional

# Time : Beats  0.60 %
# Memo : Beats 99.81 %

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 1
        curr_n = head
        while curr_n.next != None:
            curr_n = curr_n.next
            l += 1

        move = l - n

        prev_n = None
        curr_n = head

        if move == 0:
            head = head.next
        else:
            for i in range(move):
                prev_n = curr_n
                curr_n = curr_n.next

            prev_n.next = curr_n.next
        
        
        return head