'''
link : https://leetcode.com/problems/linked-list-cycle-ii/
142. Linked List Cycle II
Medium

6973

458

Add to List

Share
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Accepted
649,735
Submissions
1,474,722

'''


###########################################################

'''
TC : O(n+n)
SC : O(1)
Hare and tortoise method / Floyd's algorithm

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow,fast=head,head
        intersect=None
        if head is None:
            return head
        
        if slow.next:
            slow=slow.next
            fast=fast.next
            if fast.next:
                fast=fast.next
            else:
                return None
        else:
            return None
        
        while fast!=None and  fast.next!=None:
            
            if slow==fast:
                intersect=slow
                break
            slow=slow.next
            fast=fast.next.next
        
        if intersect is None:
            return None
        
        slow=head
        fast=intersect
        
        while True:
            if slow ==fast:
                return slow
            slow=slow.next
            fast=fast.next

################################################################

'''
Using Map/set 

TC :O(n)+O(nlogn)
SC : O(n)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        st=set()
        tmp = head
        if tmp == None:
            return head
        
        while tmp !=None:
            if tmp in st:
                return tmp
            st.add(tmp)
            tmp=tmp.next
        
        return None
        