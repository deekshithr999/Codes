# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Whhahta solnn
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        TC: 
        '''
        iter = res = ListNode()
        n1, n2 = list1, list2
        while n1 and n2:
            print("n1, n2", n1.val, n2.val)
            if n1.val > n2.val:
                iter.next = n1
                iter = iter.next
                n1 = n1.next
            else:
                iter.next = n2
                iter = iter.next
                n2 = n2.next
        
        if n1:
            iter.next = n1
        if n2:
            iter.next = n2
        return res.next