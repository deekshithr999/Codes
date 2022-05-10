'''
link : https://leetcode.com/problems/copy-list-with-random-pointer/
138. Copy List with Random Pointer
Medium

8304

964

Add to List

Share
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
Accepted
771,489
Submissions
1,609,996


'''


#################################################################################
'''
Sol 1 :
insert new nodes in after the old ones and do the mapping

TC: O(2n)
SC: O(1)

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nhead=None
        tmp=head
        while tmp!=None:
            nnode=Node(tmp.val)
            #print("nnode.val ",nnode.val)
            nnode.next=tmp.next
            tmp.next=nnode
            tmp=tmp.next.next
        if head!=None:
            nhead=head.next
        tmp=head
        while tmp!=None:
            if tmp.random !=None:
                tmp.next.random=tmp.random.next
            tmp=tmp.next.next
            
        
        otmp=head
        ntmp=nhead
        while otmp!=None:
            nntmp=otmp.next
            otmp.next=otmp.next.next
            otmp=otmp.next
            if nntmp!=nhead:
                #print("nhead : ",nhead.val)
                ntmp.next=nntmp
                ntmp=ntmp.next
# This is to remind "don't delete blindly"        
#         tmp=nhead
#         while tmp.next!=None:
#             print(tmp.val)
#             tmp.next=tmp.next.next
#             tmp=tmp.next
        
        
        
        return nhead
########################################################################
'''
Using dict/maps

TC : O(2n)
SC : O(n)

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return head
        dt={}
        dt[None]=None
        tmp=head
        while tmp!=None:
            newnode=Node(tmp.val)
            dt[tmp]=newnode
            tmp=tmp.next

        tmp=head
        while tmp!=None:
            dt[tmp].next=dt[tmp.next]
            if tmp.random:
                dt[tmp].random=dt[tmp.random]
            tmp=tmp.next
        
        return dt[head]









########################################################################

'''
Sol 2 :

Using Stacks 

TC : O(n^2+2n)
SC : O(2n)

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        ostack=[]
        tmp=head
        
        while tmp!=None:
            ostack.append(tmp)
            tmp=tmp.next
        
        nstack=[]
        tmp=head
        prev=None
        newhead=None
        while tmp!=None:
            nnode=Node(tmp.val)
            if prev!=None:
                prev.next=nnode
            if newhead==None:
                newhead=nnode
            prev=nnode
            nstack.append(nnode)
            tmp=tmp.next
        
        
        for i in range(len(ostack)):
            
            if ostack[i].random !=None:
                idx=ostack.index(ostack[i].random)
                nstack[i].random=nstack[idx]
        
        return newhead
