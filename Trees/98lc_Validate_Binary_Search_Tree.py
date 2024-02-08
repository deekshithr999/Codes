
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def trav(node, left, right):
            if node is None:
                return True
            if not (node.val <right and node.val > left) :
                return False
            return trav(node.left, left, node.val) and trav(node.right, node.val, right)
        return trav(root, float('-inf'), float('inf'))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    This is a bottom to top approach
    Idea:
    1. Min in the right subTree is always greater than parent
    2. Max in left subTree is always less than parent
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return root
        
        def trav(node):
            if node is None:
                return [True, 2**31,-2**31-1 ] #(bool, min, max)
            
            left,right = trav(node.left), trav(node.right)
            if left[0] is False:
                return left
            if right[0] is False:
                return right
            if left[2]>= node.val:
                return [False, 0,0]
            elif right[1]<=node.val:
                return [False,0,0]
            else:
                return [True, min(left[1],right[1],node.val), max(left[2], right[2],node.val)]
        res = trav(root)
        return res[0]
        