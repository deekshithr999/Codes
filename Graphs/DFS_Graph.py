

class Solution:
    '''
    Recursive Approach
    '''   
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        
        vis = [0]*V
        trav = []
        
        def dfs(v):
            trav.append(v)
            vis[v]=1
            for adjV in adj[v]:
                if vis[adjV]:
                    continue
                dfs(adjV)
        dfs(0)
        return trav

#User function Template for python3

class Solution:
    '''
    Iterative Approach
    '''
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        
        vis = [0]*V
        trav, stack = [],[]
        stack.append(0)
        
        while stack:
            top = stack.pop()
            if vis[top]:
                continue
            vis[top]=1
            trav.append(top)
            stack.extend(adj[top][::-1])
        return trav               


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends