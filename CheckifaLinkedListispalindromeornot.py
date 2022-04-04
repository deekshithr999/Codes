
'''
link : 

234. Palindrome Linked List
Easy

8372

514

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1: https://leetcode.com/problems/palindrome-linked-list/


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
Accepted
916,459
Submissions
1,980,964
'''


'''
Using Stack
TC : O(n)
SC : O(n)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        st=[]
        tmp =head
        
        while tmp is not None:
            st.append(tmp.val)
            tmp=tmp.next
        
        
        #top=st[-1]
        tmp =head
        while tmp!=None:
            top =st[-1]
            st.pop()
            
            if top!=tmp.val:
                return False
            tmp=tmp.next
            
        return True
                
        