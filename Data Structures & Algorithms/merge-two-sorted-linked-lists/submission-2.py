# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Idea, 2ptr, one at list1 head the other at list2 head
        # pick whichever one is smaller, then traverse to it's next
        # make sure all nodes are traversed through the list! 
        # If not, finish traversing at the v end
        mergedHead = ListNode()
        start = mergedHead
        
        while list1 and list2:
            if list1.val < list2.val:
                mergedHead.next = list1
                list1 = list1.next
                mergedHead = mergedHead.next
            else:
                mergedHead.next = list2
                list2 = list2.next
                mergedHead = mergedHead.next
            
        mergedHead.next = list1 if list1 else list2
        return start.next
