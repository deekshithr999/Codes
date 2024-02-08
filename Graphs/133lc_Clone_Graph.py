"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        dt = {} # num to node mapping
        vis = set()

        def dfs(node):            
            vis.add(node.val)
            dt[node.val] = dt.get(node.val, Node(node.val))
            new_node = dt[node.val]
            for neigh in node.neighbors:
                if neigh.val not in dt:
                    dt[neigh.val]=Node(neigh.val)
                new_node.neighbors.append(dt[neigh.val])
                if neigh.val not in vis:
                    dfs(neigh)
        dfs(node)
        return dt[node.val]