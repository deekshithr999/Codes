# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def pathToNode(root, val, lst):
            if root is None: return False
            lst.append(root)
            if root.val == val:
                return True
            found = pathToNode(root.left, val, lst) or pathToNode(root.right, val, lst)
            if found: return True
            lst.pop()
            return False

        srcPath, dstPath = [], []
        pathToNode(root, startValue, srcPath)
        pathToNode(root, destValue, dstPath)
        res = ""

        idx = i = 0
        while i < min(len(srcPath), len(dstPath)):
            if srcPath[i] == dstPath[i]:idx=i
            else: break
            i += 1
        
        srcV = [n.val for n in srcPath ]
        dstV = [n.val for n in dstPath]

        # not needed here
        for i in range(idx, len(srcPath)-1):
            res += 'U'

        # par -> l/r till the dest
        for i in range(idx, len(dstPath)-1):
            if dstPath[i].left == dstPath[i+1]: res += 'L'
            else: res += 'R'
        return res
