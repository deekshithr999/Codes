class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        n = len(grid)
        que = [(0,0,1)]
        inQue = set((0,0))
        minDist = float('inf')
        operations =[(1,0), (0,1), (1,1), (-1,0), (0, -1), (-1,-1), (1, -1),(-1,1)]
        while que:
            r, c, dist = que.pop(0)
            if r==n-1 and c==n-1:
                minDist = min(minDist, dist)
                continue

            for op in operations:
                if r+op[0]<0 or r+op[0]>=n:
                    continue
                if c+op[1]<0 or c+op[1]>=n:
                    continue
                if grid[r+op[0]][c+op[1]]:
                    continue
                if (r+op[0], c+op[1]) in inQue:
                    continue
                
                que.append((r+op[0], c+op[1], dist+1))
                inQue.add((r+op[0], c+op[1]))
        return -1 if minDist == float('inf') else minDist



        