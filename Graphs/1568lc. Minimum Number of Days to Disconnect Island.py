class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        cnt = self.cntIslands(grid)
        if cnt != 1: return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]: continue
                grid[i][j]=0
                cnt = self.cntIslands(grid)
                grid[i][j] = 1
                if cnt  != 1: return 1 #handles '1' only 1 island presence

        return 2
    
    def cntIslands(self, grid):
        vis = set()
        cnt = 0
        for i1 in range(len(grid)):
            for j1 in range(len(grid[0])):
                if grid[i1][j1] and (i1, j1) not in vis:
                    self.dfs(grid, vis, i1, j1)
                    cnt += 1
        return cnt

    def isValid(self, grid, r, c):
        m,n = len(grid), len(grid[0])
        return (0<=r<m) and (0<=c<n)

    def dfs(self, grid, vis, r,c):
        if (not self.isValid(grid, r, c)) or (not grid[r][c]) or ((r,c) in vis):
            return
        vis.add((r, c))
        neighs = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]

        for nr, nc in neighs:
            self.dfs(grid, vis, nr, nc)

        return
        