'''
Link : https://leetcode.com/problems/reverse-linked-list/

206. Reverse Linked List
Easy

10981

185

Add to List

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

'''
##################################################
'''
TC : O(n)
SC : O(n) # but storing the addresses instead of values
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst=[]
        tmp =head
        
        while tmp is not None:
            lst.append(tmp)
            tmp=tmp.next
        
        
        new_head=None
        if len(lst)==0:
            return head
        new_head =lst.pop()
        tmp=new_head
        while len(lst):
            tmp.next=lst.pop()
            tmp=tmp.next
            
            if(len(lst) == 0):
                tmp.next=None
        
        return new_head



##################################################
'''
Three pointer method to reverse a Linked list
SC:O(1)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prevn=None
        currn=head
        nextn=None
        
        while(currn is not None):
            
            nextn=currn.next
            currn.next=prevn
            prevn=currn
            currn=nextn
        
        return prevn
        



##################################################
'''
Using Stack
SC : O(n)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst=[]
        
        tmp =head
        while tmp!=None:
            lst.append(tmp.val)
            tmp=tmp.next
        new_lst=None
        
        if len(lst)!=0:
            new_lst=ListNode()
            new_lst.val=lst.pop()
        curr=new_lst
        while(len(lst)):
            tp=ListNode()
            tp.val=lst.pop()
            curr.next=tp
            curr=tp
        return new_lst


##################################################
'''
Recursive Approach
SC : O(n)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.newRevList(head,head,None)
    
    def newRevList(self,head,curr,new_head):
        if curr ==None:
            return new_head
        tl=ListNode()
        tl.val=curr.val
        tl.next=new_head
        new_head=tl
        return self.newRevList(head,curr.next,new_head)

##################################################
'''
Iterative Approach
SC:O(n)

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head=None
        
        temp=head
        
        while temp!=None:
            tl=ListNode()
            tl.val=temp.val
            if new_head==None :
                new_head =tl
            else:
                tl.next=new_head
                new_head =tl
            temp=temp.next
        return new_head
        