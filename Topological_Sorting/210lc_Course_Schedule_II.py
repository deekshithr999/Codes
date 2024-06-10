class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsOrder = []
        adj = {c:[] for c in range(numCourses)}
        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
        vis, path = [0]*numCourses, [0]*numCourses
        for crs in range(numCourses):
            if self.dfsWithCycleDet(crs, vis, path, adj, crsOrder):
                return []
        return crsOrder
    

    def dfsWithCycleDet(self, v, vis, path, adj, crsOrder):
        if path[v]:
            return True #cycle exists
        if vis[v]:
            return False
        vis[v] = 1
        path[v] = 1

        for neigh in adj[v]:
            if self.dfsWithCycleDet(neigh, vis, path, adj, crsOrder):
                return True
        path[v]=0
        crsOrder.append(v)
        return False


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for a,b in prerequisites:
            adj[b] = adj.get(b, [])
            adj[b].append(a)
        # print(adj)
        for crs in range(numCourses):
            if crs not in adj:
                adj[crs] = []
        stack = []
        vis, path = [0]*numCourses,[0]*numCourses

        for crs in range(numCourses):
            if not vis[crs]:
                if self.dfsWithCycle(crs, vis, path, stack, adj):
                    return []
        return stack[::-1 ]
    

    def dfsWithCycle(self, crs, vis, path, stack, adj):
        vis[crs] = 1 
        path[crs] = 1
        for neigh in adj[crs]:
            if path[neigh]:
                return True
            if not vis[neigh]:
                if self.dfsWithCycle(neigh, vis, path, stack, adj):
                    return True
        path[crs]=0
        stack.append(crs)
        return False