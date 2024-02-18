# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        '''
        TC: O(n)
        SC: O(n)
        '''
        dt = {0:1}

        def dfsTrav(node, runningSum):
            if node is None:
                return 0
            runningSum += node.val
            cnt = dt.get(runningSum-target, 0)
            dt[runningSum] = dt.get(runningSum,0)+1
            cnt += dfsTrav(node.left, runningSum)+dfsTrav(node.right, runningSum)
            dt[runningSum] -=1
            return cnt
        return dfsTrav(root, 0)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        TC: O(n^2)
        SC: O(n)
        '''

        def preOrder(node, currSum):
            if node is None:
                return 0
            tot = 0
            currSum += node.val
            if currSum == targetSum:
                tot += 1
            tot += preOrder(node.left, currSum)+preOrder(node.right, currSum)
            return tot
        
        def inorder(root):
            if root is None:
                return 0
            c = preOrder(root,0)
            c += inorder(root.left)+inorder(root.right)
            return c
        return inorder(root)