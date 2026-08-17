# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ret_list = None
        head_ret_list = None
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                aux = list1
                list1 = list1.next
                if ret_list is None:
                    ret_list = aux
                    head_ret_list = ret_list
                else:   
                    ret_list.next = aux  
                    ret_list = ret_list.next
            else:
                aux = list2
                list2 = list2.next
                if ret_list is None:
                    ret_list = aux
                    head_ret_list = ret_list
                else:
                    ret_list.next = aux
                    ret_list = ret_list.next
        
        if list1 is not None:
            if ret_list is None:
                ret_list = list1
                head_ret_list = ret_list
            else:
                ret_list.next = list1
        if list2 is not None:
            if ret_list is None:
                ret_list = list2
                head_ret_list = ret_list
            else:
                ret_list.next = list2
                ret_list = ret_list.next

        return head_ret_list