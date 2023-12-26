
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        TC: O(n)
        SC: O(1)
        '''
        def invertABTree(root):

            if root == None:
                return 
            root.left, root.right = root.right, root.left
            invertABTree(root.left)
            invertABTree(root.right)
        invertABTree(root)
        return root
        