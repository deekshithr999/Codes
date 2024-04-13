# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def inOrder(node, newNode):
            if node is None:
                return newNode
            
            tnode = inOrder(node.left, newNode)
            tnode.right = node
            tnode = node
            tnode.left = None
            #need right trav
            tnode = inOrder(node.right, tnode)
            return tnode
        newNode = TreeNode()
        inOrder(root, newNode)
        return newNode.right

        