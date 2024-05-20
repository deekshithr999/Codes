"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""



class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        cur = head
        # create a new node and add it to next of the orig ele
        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next = newNode
            cur = cur.next.next
        
        #point new nodes to new random
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        
        ncur = head.next
        #unlink the new list
        while ncur and ncur.next:
            ncur.next = ncur.next.next
            ncur = ncur.next
        return head.next

class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dt = {} #old->newnode
        cur = head
        while cur:
            dt[cur] = Node(cur.val)
            cur = cur.next
        
        for node, newNode in dt.items():
            newNode.next = dt[node.next] if node.next else None
            newNode.random = dt[node.random] if node.random else None
        return dt[head] if head else None
        