# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, marked = False, next=None):
        self.val = val
        self.next = next
        self.marked = marked

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
 
        while head is not None:
            if head.marked:
                return True
            else: 
                head.marked = True
                head = head.next
        
        return False

        
        