
'''
There exists edge from child -> par & par -> child

'''
from typing import List
class Solution:
	'''
	BFS
	'''
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [0]*V
		que = []
		
		for v in range(V):
		    if not vis[v]:
		        que.append((v,-1))
		        
		        while que:
		            ele = que.pop(0)
		            if vis[ele[0]]:
		              #  print("here")
		                return True
                    vis[ele[0]]=1
                    for ver in adj[ele[0]]:
                        if ver == ele[1]:
                            continue
                        que.append((ver, ele[0]))
                            
		return False
from typing import List
class Solution:
	'''
	DFS
	'''
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [0]*V
		
		def hasCycle(currV, par):
		    vis[currV]=1
		    
		    for v in adj[currV]:
		        if v!= par and vis[v]:
		            return True
		        if not vis[v] and hasCycle(v, currV):
		            return True
		    return False
		    
        for v in range(V):
            if not vis[v] and hasCycle(v,-1):
                return True
        return False


from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis=[0]*V
		
		def hasCycle(par, currV):
		  #  print("currV = ", currV)
		    if vis[currV]:
		        return True
		    vis[currV]=1
		    for v in adj[currV]:
		        if v!=par and  hasCycle(currV, v):
		            return True
		    return False
        for v in range(V):
            if (not vis[v]) and hasCycle(-1, v):
                return True
        return False


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends