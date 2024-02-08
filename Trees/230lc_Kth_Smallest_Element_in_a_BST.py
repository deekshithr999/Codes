# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return [0, num]
        #cnt = 0,res = 0
        def trav(node, cnt):
            if node is None:
                return [0, cnt]
            
            ele = trav(node.left, cnt)
            if ele[1]==k:
                return ele

            cnt = ele[1]+1
            if cnt == k:
                #print("node val", node.val)
                return  [node.val, cnt]
            ele = trav(node.right, cnt)
            return ele
        ele = trav(root, 0)
        return ele[0]

        