# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkByDepth(node):
            if node is None:
                return 0
            left_depth = checkByDepth(node.left)
            right_depth = checkByDepth(node.right)
            if abs(left_depth-right_depth)>1:
                return float('inf')
            return 1+max(left_depth, right_depth)
        return True if checkByDepth(root) != float('inf') else False
        