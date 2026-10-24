# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        carry = 0
        cur = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sm = v1+v2+carry
            if carry==1:
                carry-=1
            if sm>9:
                carry += 1
                sm = sm-10
            dummy.next = ListNode(val=sm)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next
        
        return cur.next
            