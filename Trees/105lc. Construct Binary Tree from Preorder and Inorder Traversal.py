# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def constructTree(inRange, preIdx):
            if inRange[1]<inRange[0]:
                return None
            #find the preNum
            for i in range(inRange[0], inRange[1]+1):
                if preorder[preIdx[0]] == inorder[i]:
                    break
            par = TreeNode()
            preIdx[0] += 1
            lc = constructTree([inRange[0],i-1], preIdx)
            rc = constructTree([i+1, inRange[1]], preIdx)
            par = TreeNode(inorder[i], lc, rc)
            return par
        return constructTree([0, len(inorder)-1], [0])
