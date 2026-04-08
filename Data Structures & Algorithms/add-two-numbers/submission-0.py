# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getInt(ls):
            value = ''
            while ls:
                value += str(ls.val)
                ls = ls.next
            return ''.join(reversed(value)) # need to reverse list so it's the correct sum (remember that the linked list is in reverse)
        num1 = int(getInt(l1))
        num2 = int(getInt(l2))
        sumVal = [int(num) for num in str(num1+num2)]
        res = ListNode(val=sumVal.pop())
        head = res
        while sumVal:
            head.next = ListNode(val=sumVal.pop())
            head = head.next
        return(res)
        
