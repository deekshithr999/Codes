# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        cost = 0

        def postOrder(root):
            nonlocal cost
            if not root:
                return 0
            lexcess, rexcess = postOrder(root.left), postOrder(root.right)
            cost += abs(lexcess)+abs(rexcess)
            return lexcess+rexcess+root.val-1
        postOrder(root)
        return cost