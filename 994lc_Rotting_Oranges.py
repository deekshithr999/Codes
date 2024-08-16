class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        vis = [ [0]*len(grid[0]) for _ in range(len(grid))]
        nFresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i,j))
                if grid[i][j] == 1:
                    nFresh += 1
        t = 0

        def isValid(r, c, vis, grid):
            m,n = len(grid), len(grid[0])
            return 0<=r<m and 0<=c<n and grid[r][c] == 1 and not vis[r][c]
        
        adj = [(0,-1), (0,1), (-1,0), (1,0)]
        while dq and nFresh:
            dqSize = len(dq)
            for _ in range(dqSize):
                r, c = dq[0]
                dq.popleft()
                for a, b in adj:
                    if isValid(r+a, c+b, vis, grid):
                        vis[r+a][c+b] = 1
                        dq.append((r+a, c+b))
                        nFresh -= 1
            t += 1
        return t if nFresh==0 else -1l