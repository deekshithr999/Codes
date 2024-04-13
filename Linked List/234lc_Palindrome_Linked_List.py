# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Too many border cases
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        
        def revLinkedList(head):
            prev,curr, next = None, head, None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        # if odd head traverses till mid, and mid.next is None
        # and gets terminated
        def compLists(head1, head2):
            # second mid gets pointed to None 
            while head1 and head2:
                if head1.val != head2.val:
                    return False
                head1 = head1.next
                head2 = head2.next
            return True
        
        revMidHead = revLinkedList(mid)
        return compLists(head, revMidHead)