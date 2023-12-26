class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here
		vis = [0]*V
		
		def dfs(fromV, vis):
		    vis[fromV]=1
		    
		    for toV in adj[fromV]:
		        if vis[toV]:
		            continue
		        dfs(toV, vis)
		lastV = 0 # don't check for sum everytime
	    for v in range(V):
	        if vis[v]:
	            continue
	        lastV=v
	        dfs(v, vis)
	   
	    newVis = [0]*V
	    dfs(lastV, newVis)
	    for ele in newVis:
	        if not ele:
	            return -1
	    return lastV
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends