# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        st = set(to_delete)
        res = []

        def postOrder(root, noPar):
            if not root: return
            toDel = (root.val in st)
            root.left = postOrder(root.left, toDel)
            root.right = postOrder(root.right, toDel)
            if (not (root.val in st)) and noPar:
                res.append(root)
            return root if (root.val not in st) else None
        postOrder(root, True)
        return res



class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root: return []
        res = [root]

        for delVal in to_delete:
            j = 0
            while j < len(res):
                if res[j].val == delVal:
                    r = res[j]
                    if r.left: res.append(r.left)
                    if r.right: res.append(r.right)
                    res.remove(r)
                    break
                self.removeNode(res[j], delVal, res, None, 'A')
                j += 1
        return res
                
    
    def removeNode(self, root, nodeVal, roots, par, whichDir):
        if not root:
            return
        if root.val == nodeVal:
            if root.left: roots.append(root.left)
            if root.right: roots.append(root.right)
            if par and whichDir=='L': par.left= None
            if par and whichDir == 'R': par.right = None
            return
        
        self.removeNode(root.left, nodeVal, roots, root, 'L')
        self.removeNode(root.right, nodeVal, roots, root, 'R')
        