'''
61. Rotate List
Medium

4922

1265

Add to List

Share
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
Accepted
541,801
Submissions
1,557,304

'''
########################################################
'''
Similar to below 
Just using simple recursion

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listlen(self,head):
        cnt=0
        tmp=head
        while tmp!=None:
            cnt+=1
            tmp=tmp.next
        return cnt
    def getNonenode(self, head,val):
        if val==1:
            return head
        return self.getNonenode(head.next,val-1)
    
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        le=self.listlen(head)
        rem=k%le
        if rem == 0:
            return head
        
        newhead=None
        val=le-rem
        nodetonone =self.getNonenode(head,val)
        
#         while val <= le-rem-1:
#             val=val+1
#             nodetonone=nodetonone.next

        
        newhead=nodetonone.next
        nodetonone.next=None
        
        tmp=newhead
        while tmp.next!=None:
            tmp=tmp.next
        
        tmp.next=head
        return newhead
            
            


########################################################



'''
TC : O(n)
SC : O(1)

Search for pointer from where the newhead starts
Then add before the head


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listlen(self,head):
        cnt=0
        tmp=head
        while tmp!=None:
            cnt+=1
            tmp=tmp.next
        return cnt
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        le=self.listlen(head)
        rem=k%le
        if rem == 0:
            return head
        
        newhead=None
        val=1
        nodetonone =head
        while val <= le-rem-1:
            val=val+1
            nodetonone=nodetonone.next
        
        newhead=nodetonone.next
        nodetonone.next=None
        
        tmp=newhead
        while tmp.next!=None:
            tmp=tmp.next
        
        tmp.next=head
        return newhead
            



########################################################


'''
TC : O(n)
SC : O(1)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listlen(self,head):
        cnt=0
        tmp=head
        while tmp!=None:
            cnt+=1
            tmp=tmp.next
        return cnt
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        le=self.listlen(head)
        k=k%le
        cnt=1
        while cnt<=k:
            tmp=head
            prevval=-9999
            while tmp!=None:
                if prevval==-9999:
                    prevval=tmp.val
                else:
                    cval=tmp.val
                    tmp.val=prevval
                    prevval=cval
                tmp=tmp.next
            if head !=None and head.next!=None:
                head.val=prevval
            cnt+=1
        return head