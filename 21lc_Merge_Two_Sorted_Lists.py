'''
Link : https://leetcode.com/problems/merge-two-sorted-lists/

21. Merge Two Sorted Lists
Easy

11388

1025

Add to List

Share
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
Accepted
2,048,537
Submissions
3,418,348

'''

'''
Concise code for the below
TC :O(n)
SC :O(1)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None :
            return list2
        if list2 is None:
            return list1
        
        if list1.val>list2.val:
            list1,list2=list2,list1
        
        res =list1
        
        while list1!=None and list2!=None:
            tmp=None
            while (list1!=None) and (list1.val<=list2.val):
                tmp=list1
                list1=list1.next
            
            tmp.next=list2
            list1,list2=list2,list1
        return res
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        TC: O(n)
        SC: O(1)
        '''
        if not list1:
            return list2
        if not list2:
            return list1
        newtmp = newHead = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                newtmp.next= list1
                list1 = list1.next
            else:
                newtmp.next = list2
                list2 = list2.next
            newtmp = newtmp.next
        if list1:
            newtmp.next = list1
        if list2:
            newtmp.next = list2

        return newHead.next
        

'''
Take one list as the final and keep adding elements into it

TC : O(n)
SC : O(1)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list1 == None):
            return list2
        elif list2 == None:
            return list1
        
        l1p,l1c=None,list1
        l2p,l2c=None,list2
        head =list2
        while l1c is not None and l2c is not None:
            
            if l1c.val < l2c.val:
                
                l1p=l1c
                l1c=l1c.next
                
                if l2p is None:
                    l1p.next=l2c
                    l2p=l1p
                    head=l1p
                else :
                    l1p.next=l2c
                    l2p.next=l1p
                    l2p=l2p.next #increment the previous pointer of l2
            else:
                l2p=l2c
                l2c=l2c.next
            
        if l1c is not None:
            
            l2p.next=l1c
        return head 
                
                

'''

Create a new list and keep adding the smallest of the 2
TC : O(n)
SC : O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = None
        tnew=None
        t1=list1
        t2=list2
        
        while (t1!=None) and (t2!=None):
            
            if t1.val<t2.val:
                
                tnode=ListNode(t1.val)
                t1=t1.next
                if tnew is None:
                    newhead=tnode
                    tnew=newhead
                else:
                    tnew.next=tnode
                    tnew=tnew.next
            else:
                tnode=ListNode(t2.val)
                t2=t2.next
                if tnew is None:
                    newhead=tnode
                    tnew=newhead
                else:
                    tnew.next=tnode
                    tnew=tnew.next
        while t1!= None:
                tnode=ListNode(t1.val)
                t1=t1.next
                if tnew is None:
                    newhead=tnode
                    tnew=newhead
                else:
                    tnew.next=tnode
                    tnew=tnew.next
        
        while t2!=None:
                tnode=ListNode(t2.val)
                t2=t2.next
                if tnew is None:
                    newhead=tnode
                    tnew=newhead
                else:
                    tnew.next=tnode
                    tnew=tnew.next
        return newhead
            
            
                
        