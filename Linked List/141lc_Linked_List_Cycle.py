# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head
        while fast and fast.next: #base case covered here, head is null
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


class Solution:
    '''
    Using Set to find the duplicate

    TC : O(n)
    SC : O(n)

    '''

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st=set()
        
        tmp = head
        while tmp!=None:
            if tmp in st:
                return True
            st.add(tmp)
            tmp=tmp.next
        
        return False