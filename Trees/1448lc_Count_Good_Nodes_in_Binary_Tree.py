# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def trav(node,  currMax):
            if node is None:
                return 0
            tcnt = 0
            if node.val >= currMax:
                currMax = node.val
                tcnt += 1
            tcnt +=trav(node.left,  currMax)+trav(node.right,  currMax)
            return tcnt
        return trav(root, -10**4+1)