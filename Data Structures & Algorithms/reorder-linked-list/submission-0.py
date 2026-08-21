# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        half = head
        full = head.next

        while full is not None and full.next is not None:
            full = full.next.next
            half = half.next

        curr = half.next
        half.next = None 

        prev = None
        while curr is not None:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux

        half = prev
        start = head

        while half is not None:
            aux1 = start
            aux2 = half
            start = start.next
            half = half.next
            
            aux1.next = aux2
            aux2.next = start
            

            


        

        
        