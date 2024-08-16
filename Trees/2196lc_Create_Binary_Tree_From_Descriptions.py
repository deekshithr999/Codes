# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if not descriptions: return None
        dt = {}
        st = set()

        for p, c, isLeft in descriptions:
            st.add(c)
            if p not in dt:
                dt[p] = TreeNode(p)
            if c not in dt:
                dt[c] = TreeNode(c)
            pNode, cNode = dt[p], dt[c]

            if isLeft:
                pNode.left = cNode
            else:
                pNode.right = cNode


        for p, c, _ in descriptions:
            if p not in st:
                return dt[p]