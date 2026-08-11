# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Idea: Ptr 1 starting at list2, Ptr 2 starting at list 2
        # Move the pointer based on which one is smaller, 
        # i.e. list 1 starts with 1, list 2 starts with 1, 
        # We add 1 from list1, then move ptr 1 and compare the next value
        # IF they're the same value, add both + move both ptrs
        # IF one list finishes before the other, loop the remaining values
        ptr1 = list1
        ptr2 = list2
        result = ListNode()
        current = result
        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                current.next = ptr1
                current = current.next
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                current = current.next
                ptr2 = ptr2.next
        
        if ptr1 != None:
            current.next = ptr1
        if ptr2 != None:
            current.next = ptr2
        return result.next
        