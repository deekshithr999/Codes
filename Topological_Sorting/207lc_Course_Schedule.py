class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = dict()
        for a, b in prerequisites:
            adj[b] = adj.get(b, [])
            adj[b].append(a)
        for c in range(numCourses):
            adj[c] = adj.get(c, [])
        # print(adj)
        vis, path = [0]*numCourses, [0]*numCourses
        for c in range(numCourses):
            if not vis[c]:cycle = self.dfsCycle(c, path, vis, adj)
            # print("path ", path)
            if cycle:
                # print("cycle existss at c", c)
                return False
        return True
    
    def dfsCycle(self, v, path, vis, adj):
        vis[v] = 1
        path[v]=1 # add to path
        # print("adding ", v,  " to path")
        for neigh in adj[v]:
            if path[neigh]:return True
            if not vis[neigh]:
                ret =  self.dfsCycle(neigh, path, vis, adj) #edged here
                if ret:
                    return True
        path[v] = 0 #remove from path
        # print("Remove ", v,  " to path")
        return False
     