
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis = [0]*V
        path = [0]*V
        
        def dfsHasCycle(currV):
            path[currV]=1
            vis[currV]=1
            for v in adj[currV]:
                if (not vis[v]) and dfsHasCycle(v):
                        return True
                if path[v]:
                    return True
            path[currV]=0
            return False
            
        for v in range(V):
            if not vis[v] and dfsHasCycle(v):
                return True
                
        return False
    

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis = [0]*V
        path = [0]*V
        
        def dfsHasCycle(currV):
            
            if path[currV]:
                return True
            if vis[currV]:
                return False
            
            vis[currV]=1
            path[currV]=1
            for v in adj[currV]:
                if dfsHasCycle(v):
                    return True
            path[currV]=0
            return False
        
        for v in range(V):
            if not vis[v] and dfsHasCycle(v):
                return True
        return False

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited = set()
        track_connected = set()
        
        def dfsHasCycle(currV):
            if currV in visited:
                return True
            track_connected.add(currV)
            visited.add(currV)
            for v in adj[currV]:
                if dfsHasCycle(v):
                    return True
            visited.remove(currV)
            return False
        
        for v in range(V):
            if v not in track_connected:
                if dfsHasCycle(v):
                    return True
        return False



class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        def dfsHasCycle(startV, currV, visited):
            if visited[currV]:
                return False
            for v in adj[currV]:
                if v == startV:
                    return True
                if dfsHasCycle(startV, v, visited):
                    return True
            return False
        
        print("lets start")
        for v in range(V):
            visited =[0]*V
            print("vert ", v)
            if dfsHasCycle(v, v, visited):
                return True
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends