# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def travToCheck(node1, node2):
            if node1== None and node2==None:
                return True
            if node1 and node2 and node1.val == node2.val:
                return travToCheck(node1.left, node2.left) and travToCheck(node1.right, node2.right)
            return False
        return travToCheck(p,q) 
        