from typing import List, Optional

# Time : Beats 16.62 %
# Memo : Beats 68.28 %

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_2_lists(list1, list2):
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
                    return head.next
                elif not list2:
                    current.next = list1
                    return head.next
                else:    
                    if list1.val < list2.val:
                        current.next = list1
                        list1 = list1.next
                    else:
                        current.next = list2
                        list2 = list2.next
                current = current.next
            return head.next

        if not lists:
            return None
        while len(lists) != 1:
            L, R = 0, len(lists)-1
            new_list = []
            while L<=R:
                if L==R:
                    new_list.append(lists[L])
                else:
                    merged = merge_2_lists(lists[L], lists[R])
                    new_list.append(merged)
                L += 1
                R -= 1
            lists = new_list

        return lists[0]