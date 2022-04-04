'''
link : https://leetcode.com/problems/linked-list-cycle/

141. Linked List Cycle
Easy

7668

767

Add to List

Share
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

Accepted
1,368,383
Submissions
2,995,366

'''
############################################################

'''
Sol :
Using Floyd's algorithm
Hare and tortoise method
Slow and fast pointer

TC : O(n)
SC:O(1)

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow,fast=head,head
        
        if fast and (fast.next):
            fast=fast.next.next
            slow=slow.next
        while fast!=None and fast.next!=None:
            
            if slow is fast:
                return True
            
            slow=slow.next
            fast=fast.next.next
        
        return False



############################################################

'''
Using Set to find the duplicate

TC : O(n)
SC : O(n)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st=set()
        
        tmp = head
        while tmp!=None:
            if tmp in st:
                return True
            st.add(tmp)
            tmp=tmp.next
        
        return False
        