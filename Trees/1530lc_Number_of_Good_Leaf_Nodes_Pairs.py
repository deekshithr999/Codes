# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        paths = []
        res = 0
        def preOrder(root, paths, path):

            if root is None: return
            if root.left == None and root.right == None:
                paths.append(path)
            preOrder(root.left, paths, path+'L')
            preOrder(root.right, paths, path+'R')
        
        def findDist(p1, p2):
            i = 0
            while i < min(len(p1), len(p2)):
                if p1[i] != p2[i]: break
                i += 1
            dist = len(p1) + len(p2)-2*i
            return dist

        preOrder(root, paths, '')

        for i in range(len(paths)):
            for j in range(i+1, len(paths)):
                if findDist(paths[i], paths[j]) <= distance:
                    res += 1
        return res