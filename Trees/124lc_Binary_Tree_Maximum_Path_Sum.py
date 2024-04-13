# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    TC:O(n)
    SC: O(n)
    '''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        def postOrder(node):# tup: (runningMax, overallMax):
            if node is None:
                return (-1001, -10001)
            
            r1,o1 = postOrder(node.left)
            r2,o2 = postOrder(node.right)
            rMax = max(r1+node.val, r2+node.val, node.val) #only a linear path
            oMax = max(o1, o2, rMax, r1+r2+node.val) #including curve
            return (rMax, oMax)
        return postOrder(root)[1]

