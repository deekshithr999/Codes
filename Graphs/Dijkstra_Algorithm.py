class Solution:
    '''
    Using Heap implementation

    Note: heapq module in python is a min heap implementation
    Idea: vis[] can be removed by comparing the curr distance > dist[vertex]'
    '''

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        import heapq
        minHeap =[]
        dist = [float('inf')]*V
        dist[S]=0
        heapq.heappush(minHeap, (0,S))
        vis = [0]*V
        while minHeap:
            FromC, FromV = heapq.heappop(minHeap)
            if vis[FromV]:
                continue
            vis[FromV]=1
            for ele in adj[FromV]:
                toV, toW = ele[0], ele[1]
                if dist[toV]> FromC + toW:
                    dist[toV]= FromC+toW
                    heapq.heappush(minHeap, (dist[toV], toV))
                    
        return dist
                    
class Solution:
    '''
    Using Visited Vertex
    '''
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        vis  = [0]*V
        dist = [float('inf')]*V
        dist[S]=0
        
        while True:
            FromV, FromC = -1, float('inf')
            # Select the vertex with min edge weight & not visited
            for v in range(V):
                if not vis[v] and dist[v] < FromC:
                    FromV, FromC = v, dist[v]
            
            if FromV == -1: # All are visited & there are few un reachable
                return dist
            vis[FromV]=1
            for i in adj[FromV]:
                toV, toW = i[0], i[1]
                if dist[toV] > FromC + toW:
                    dist[toV]= FromC+toW
        
        return dist 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()