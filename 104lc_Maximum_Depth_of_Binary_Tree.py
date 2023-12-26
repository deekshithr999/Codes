# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        TC: O(n)
        SC: O(n)
        '''
        if not root :
            return 0
        stack = []
        max_depth = 0
        stack.append((root,1))
        while stack:
            node, cdepth = stack.pop()

            if node:
                max_depth = max(max_depth, cdepth)
                stack.append((node.right, cdepth+1))
                stack.append((node.left, cdepth+1))
        return max_depth
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        TC: O(n)
        SC: O(1)
        '''
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        TC: O(n)
        SC: O(n)
        '''
        if not root:
            return 0
        max_depth = 1
        curr_depth = 1
        stack = [root]
        visited = {root}
        while stack:
            top = stack[-1]
            if top.left != None and top.left not in visited:
                    stack.append(top.left)
                    visited.add(top.left)
                    curr_depth +=1
                    max_depth = max(max_depth, curr_depth)
            elif top.right != None and top.right not in visited:
                    stack.append(top.right)
                    visited.add(top.right)
                    curr_depth +=1
                    max_depth = max(max_depth, curr_depth)

            else:
                stack.pop()
                curr_depth -=1
        return max_depth


        