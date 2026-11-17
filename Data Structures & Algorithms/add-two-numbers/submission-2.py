# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        spillover = 0
        
        while l1 or l2 or spillover:
            summ = 0
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
            if spillover==1:
                summ+=1
            if summ>=10:
                spillover = 1
                summ = summ-10
            else:
                spillover = 0
            
            cur.next = ListNode(val=summ)
            cur = cur.next
        return dummy.next