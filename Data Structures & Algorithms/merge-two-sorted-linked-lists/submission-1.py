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
        head1 = list1
        head2 = list2
        
        while head1 and head2:
            if head1.val < head2.val:
                mergedHead.next = head1
                head1 = head1.next
                mergedHead = mergedHead.next
            else:
                mergedHead.next = head2
                head2 = head2.next
                mergedHead = mergedHead.next
            
        while head1:
            mergedHead.next = head1
            mergedHead = mergedHead.next
            head1 = head1.next
        while head2:
            mergedHead.next = head2
            mergedHead = mergedHead.next
            head2 = head2.next
        return start.next
