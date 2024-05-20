'''
link : https://leetcode.com/problems/add-two-numbers/
'''

######################################################



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        c1,c2,c3 = l1, l2, res
        carry = 0

        while c1 or c2 or carry:
            tot = c1.val if c1 else 0
            tot += c2.val if c2 else 0
            tot += carry
            carry = tot//10
            tot = tot%10
            newNode = ListNode(tot)
            c3.next = newNode
            c3 = c3.next
            c1 = c1.next if c1 else c1
            c2 = c2.next if c2 else c2
        return res.next
            
        
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