# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1 Iteration
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy =  ListNode()
        dummy.next = head
        l,r = dummy, head
        while n > 0 and r:
            r = r.next
            n -=1
        while r :
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return dummy.next


class Solution:
    '''
    2 Iterations
    # Not that Amazing
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=0
        prev, curr = None, head
        tot = 0
        while curr:
            tot += 1
            curr = curr.next
        n = tot-n+1

        curr = head
        while curr:
            k += 1
            if k == n:
                if prev is None:
                    return curr.next
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next