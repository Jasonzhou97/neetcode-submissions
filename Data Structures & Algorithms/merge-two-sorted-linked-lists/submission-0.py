# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 , cur2 = list1, list2
        
        dummy = ListNode()
        dum = dummy
        while cur1 and cur2:
            if cur1.val<cur2.val:
                dummy.next = cur1
                cur1 = cur1.next
            else:
                dummy.next = cur2
                cur2 = cur2.next
            dummy = dummy.next
        while cur1:
            dummy.next = cur1
            cur1 = cur1.next
            dummy = dummy.next
        while cur2:
            dummy.next = cur2
            cur2 = cur2.next
            dummy = dummy.next
        return dum.next