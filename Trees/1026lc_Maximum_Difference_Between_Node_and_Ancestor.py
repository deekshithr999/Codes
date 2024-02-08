# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def findMax(node, path):
            if node is None:
                return 0
            max_diff = 0
            for ele in path:
                max_diff = max(max_diff, abs(ele.val - node.val))
            path.append(node)
            max_diff = max(max_diff, max(findMax(node.left, path), findMax(node.right, path)))
            path.pop()
            return max_diff
        return findMax(root, [])           
        