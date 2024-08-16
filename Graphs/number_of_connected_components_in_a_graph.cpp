class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> adj[n];
        for (auto edge : edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        vector<int> vis(n,0);
        int ncomponents = 0;
        for (int i =0; i< n; i++){
            if (!vis[i]){
                ncomponents ++;
                dfs(i, vis, adj);
            }
        }
        return ncomponents;
    }

    void dfs(int v, vector<int> & vis, vector<int> adj[]){
        if (vis[v]) return;
        vis[v]=1;
        for(auto neigh: adj[v]){
            dfs(neigh, vis, adj);
        }
        return;
    }
};
