# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        path = []
        def trav(node, stack):
            nonlocal path
            if node == None:
                return
            if node.val == start:
                stack.append(node)
                path = stack[:]
                return
            else:
                stack.append(node)
                trav(node.left, stack)
                trav(node.right, stack)
                stack.pop()
        
        def findDepth(node):
            if node == None or node.val == start:
                return 0
            return 1+max(findDepth(node.left), findDepth(node.right))
        
        trav(root,[])

        prev=top_ele = path.pop()
        max_depth = max(findDepth(top_ele.left), findDepth(top_ele.right))
        max_depth = max(max_depth, len(path))
        curr = 0
        while path:
            top_ele = path.pop()
            curr +=1
            if top_ele.left != prev:
                max_depth = max(max_depth, curr+findDepth(top_ele.left))
            else:
                max_depth = max(max_depth, curr+findDepth(top_ele.right))
            prev = top_ele
        return max_depth