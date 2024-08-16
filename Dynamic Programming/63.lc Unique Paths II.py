class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]: return 0
        # come from top , left
        pathCnt = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        pathCnt[0][0] = 1
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c]:
                    continue #do nothing
                if self.isValidCell(m, n, r-1, c):#coming From Top
                    pathCnt[r][c] += pathCnt[r-1][c]
                if self.isValidCell(m, n, r, c-1): #coming from Left
                    pathCnt[r][c] += pathCnt[r][c-1]
        return pathCnt[m-1][n-1]


                    
    def isValidCell(self, m, n, r, c):
        return (0<=r<m) and (0<=c<n)