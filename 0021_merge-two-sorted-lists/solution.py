from typing import Optional

# Time : Beats  1.48 %
# Memo : Beats 99.99 %

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return None
        if list1 != None and list2 == None:
            return list1
        if list1 == None and list2 != None:
            return list2
        
        head = ListNode()
        current = head
        while list1 or list2:
            if not list1:
                current.next = list2
                list2 = list2.next
            elif not list2:
                current.next = list1
                list1 = list1.next
            else:    
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
            current = current.next

        return head.next