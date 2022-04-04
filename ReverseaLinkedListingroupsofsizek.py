'''
link : https://leetcode.com/problems/reverse-nodes-in-k-group/

25. Reverse Nodes in k-Group
Hard

6720

480

Add to List

Share
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

Accepted
494,243
Submissions
974,317

'''

####################################################################3
'''
TC : O(n)
SC : O(n)

Use the prevhead,prevtails to store 

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k==1:
            return head
        
        phead,ptail=None,None
        chead,ctail=None,None
#        prev,curr,nxt=None,None,None
        cnt=0
        ctail=head
        it=0
        newhead=head
        while ctail!=None:
            cnt+=1
            if cnt==1:
                chead=ctail
                ctail=ctail.next
            elif cnt==k:
                it+=1
                if phead !=None:
                    phead.next=ctail
                if it==1:
                    newhead=ctail
                phead=chead
                ptail=ctail
                prev,curr,nxt=None,None,None
                curr=chead
                tmp=ctail.next
                #check for the loop here
                while prev!=ctail:
                    cnt+=1
                    nxt=curr.next
                    curr.next=prev
                    prev=curr
                    curr=nxt
                ctail=tmp
           #lets travel till the end and then reverse the curr
           #buddy
            else:
                ctail=ctail.next
            cnt=cnt%k
        
        if cnt ==0:
            phead.next=None
        else:
            phead.next=chead
        return newhead
        



####################################################################3
'''
TC : O(n)
SC : O(3n)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 1:
            return head
        
        st = set()
        tmp =head
        toadd=head
        cnt=0
        
        while tmp is not None:
            cnt+=1
            if cnt==k:
                st.add(toadd)
                toadd=tmp.next
                cnt=cnt%k
            tmp=tmp.next
        
        old_heads = []
        new_heads =[]
        cnt=0
        tmp=head
        
        while tmp!=None:
            cnt+=1
            cnt=cnt%k
            if cnt==1:
                old_heads.append(tmp)
            elif cnt==0:
                new_heads.append(tmp)
            tmp=tmp.next
        
        if cnt!=0:
            nh = old_heads[-1]
            old_heads.pop()
            new_heads.append(nh)
        else:
            new_heads.append(None)
        
        tmp=head
        cnt=0
        prev,curr,nxt=None,head,None
        
        while curr!=None:
            cnt+=1
            if cnt == 1 and curr not in st:
                break   
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            cnt=cnt%k
        
            
        while len(old_heads)!=0:
            
            old_top=old_heads[-1]
            old_heads.pop()
            new_top=new_heads[-1]
            new_heads.pop()
            
            old_top.next=new_top
        
        new_top=new_heads[-1]
        new_heads.pop()
        return new_top 