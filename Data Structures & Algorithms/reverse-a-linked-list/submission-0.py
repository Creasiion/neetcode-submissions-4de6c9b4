# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Get a temp variable + set it to a node's next
        # move that node's next to the prev value
        # Since we don't have access to their old next,
        # we use temp for this reason!
        # Would also need a prev value so then it can go
        # head.next = prev
        # prev = head
        # head = temp (something along those lines)
        curr = head
        nextNode = ListNode()
        prev = None
        res = []
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    
        