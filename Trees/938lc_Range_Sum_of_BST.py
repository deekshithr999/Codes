# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        curr_sum = 0
        if low<= root.val <=high:
            curr_sum = root.val
        return curr_sum + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)