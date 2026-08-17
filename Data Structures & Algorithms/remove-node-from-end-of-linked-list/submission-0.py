# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pnt = head
        count = 0
        while pnt is not None:
            count += 1
            pnt = pnt.next
        
        pnt = head
        prev = None
        target = count - n

        if target == 0:
            head = pnt.next
            return head

        while target != 0:
            prev = pnt
            pnt = pnt.next
            target -= 1

        prev.next = pnt.next
        return head


            




        