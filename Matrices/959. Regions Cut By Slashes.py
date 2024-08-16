class Solution:
    
    
    def expandGridsBy3(self, grid: List[str]):
        ROWS, COLS = len(grid), len(grid[0])
        mat = [[1]*3*COLS for _ in range(3*ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ' ': continue
                eRowStart, eColStart = r*3, c*3

                # \ -> start from start
                i, j = eRowStart, eColStart
                if grid[r][c] == '\\':
                    while i < eRowStart+3:
                        mat[i][j] = 0
                        i += 1
                        j += 1

                # / -> start from end
                if grid[r][c] == '/':
                    i, j = eRowStart, eColStart+2
                    while i < eRowStart+3:
                        mat[i][j] = 0
                        i += 1
                        j -= 1
        return mat


    def regionsBySlashes(self, grid: List[str]) -> int:
        mat = self.expandGridsBy3(grid)
        diskomp = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    diskomp += 1
                    self.dfs(mat, i, j)
        return diskomp
    
    def isValid(self, mat, r, c):
        rows, cols = len(mat), len(mat[0])
        return (0<=r<rows) and (0<=c<cols)

    def dfs(self, mat, r, c):

        neighs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for dr, dc in neighs:
            if self.isValid(mat, r+dr, c+dc) and mat[r+dr][c+dc]:
                mat[r+dr][c+dc] = 0
                self.dfs(mat, r+dr, c+dc)