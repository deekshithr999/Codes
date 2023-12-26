# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def maxDiameter(root):
            '''
            TC: O(n)
            SC: O(1)
            '''
            if not root:
                return 0, 0 #diam, depth
            
            ldia, ldep = maxDiameter(root.left)
            rdia, rdep = maxDiameter(root.right)
            return max(ldia, rdia, ldep+rdep), 1+max(ldep, rdep)
        mx_dia,_ = maxDiameter(root)
        return mx_dia
        