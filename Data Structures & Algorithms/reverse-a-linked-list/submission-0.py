# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == []:
            return []
        
        first = head
        second = None

        while first:
            aux = first.next
            first.next = second
            second = first
            first = aux
        
        return second

        