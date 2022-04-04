'''
link : https://leetcode.com/problems/middle-of-the-linked-list/

876. Middle of the Linked List
Easy

4863

120

Add to List

Share
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
Accepted
587,565
Submissions
812,079
'''
############################################

'''
Same as below

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        slow=fast=head
        while fast.next:
                fast=fast.next
                if fast.next:
                    fast=fast.next
                slow=slow.next
        
        return slow


############################################
'''
TC : O(n)
SC : O(1)
Using 2 pointer method . 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        prev =head
        curr=head
        inc = 1
        
        while(curr.next is not None):
            if inc:
                prev=prev.next
            curr=curr.next
            inc=(inc+1)%2
        
        return prev
        
        



################################################
'''
TC : O(2n)
SC : O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        length=-1
    
        tmp=head
        while tmp!=None:
            length+=1
            tmp=tmp.next

        length=int(math.ceil(length/2))

        tmp =head
        ci=0
        while ci!=length:
            tmp=tmp.next
            ci+=1

        return tmp

