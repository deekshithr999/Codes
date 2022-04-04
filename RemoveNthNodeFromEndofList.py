'''
link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

19. Remove Nth Node From End of List
Medium

9205

437

Add to List

Share
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

'''
##################################################
'''
Use the dummy pointer at the head and implement as below

'''

##################################################

'''
Sol 

TC : O(n)
SC : O(1)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        st:ListNode =[]
        tmp=head
        
        while tmp!=None:
            st.append(tmp)
            tmp=tmp.next
        
        top=0
        nxtnode=None
        tmp=head
        
        while len(st):
            top+=1
            tp=st.pop()
            #print("popping !")
            if top==n:
                #print("Got it!")
                nxtnode=tp
                #nxtnode=nxtnode.next
            elif top>n:
                print("Deleted it")
                tp.next=nxtnode.next
                del nxtnode
                break
            
        if top==n:
                tmp =head.next
                del head
                return tmp
        return head
            

##################################################
'''
Sol :
Tc : O(2n)
SC : O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        to_del=self.calLength(head)-n+1
        
        prev=None
        curr=head
        tlen=1
        while curr !=None:
            if tlen == to_del:
                if prev is None:
                    return curr.next
                else:
                    prev.next=curr.next
                    del curr
                    return head
            else:
                prev=curr
                curr=curr.next
                tlen+=1
            
    
    
    def calLength(self,head:Optional[ListNode])->int:
        
        tmp=head
        l=0
        while tmp!=None:
            l+=1
            tmp=tmp.next
        return l
        
        