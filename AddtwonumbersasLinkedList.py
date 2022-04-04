'''
link : https://leetcode.com/problems/add-two-numbers/

 Add Two Numbers
Medium

17384

3622

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
Accepted
2,630,911
Submissions
6,859,199
'''

######################################################
''' 
Sol :

TC : O(n)
SC : O(n)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        it1=l1
        it2=l2
        carry = 0
        newhead = None
        curr= None
        
        while it1 != None and it2 != None:
            
            s= (it1.val + it2.val + carry)%10
            carry = int((it1.val+it2.val+carry)/10)
            tnode = ListNode()
            tnode.val =s
            if newhead is None:
                newhead = tnode
                curr=newhead
            else:
                curr.next=tnode
                curr=curr.next
            it1=it1.next
            it2=it2.next
        
                    
        while it1 != None:
            tnode = ListNode()
            s= (it1.val+carry)%10
            carry = int((it1.val+carry)/10)
            tnode.val=s
            curr.next=tnode
            curr=curr.next
            it1=it1.next
        
        
        while it2!=None:
            tnode=ListNode()
            s=(it2.val+carry)%10
            carry=int((it2.val+carry)/10)
            tnode.val=s
            curr.next=tnode
            curr=curr.next
            it2=it2.next
            
        
        if carry:
            tnode =ListNode()
            tnode.val = carry
            curr.next=tnode
            carry = 0
        return newhead