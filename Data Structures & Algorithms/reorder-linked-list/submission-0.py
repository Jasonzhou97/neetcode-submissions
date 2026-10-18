# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node1 , node2 = head,head
        length = 0
        dummy1 = head
        while dummy1:
            length += 1
            dummy1 = dummy1.next

        for i in range((length-1)//2):
            node1 = node1.next
        node2 = node1.next
        node1.next = None
        
        def reverse(cur):
            dummy = cur
            prev = None
            while cur:
                next1 = cur.next
                cur.next = prev
                prev = cur
                cur = next1
            
            return prev
        
        node2 = reverse(node2)

        def merge(node1,node2):
            node = ListNode()
            while node1 and node2:
                n1,n2 = node1.next,node2.next
                node.next = node1
                node.next.next = node2
                node = node.next.next
                node1 = n1
                node2 = n2
            if node1:
                node.next = node1
                node = node.next
            if node2:
                node.next = node2
                node = node.next
            return node
        
        merge(head,node2)
