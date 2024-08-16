class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def magic(row, col):
            #unique
            vals = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if grid[i][j] in vals or not (0<grid[i][j]<=9):
                        return 0
                    vals.add(grid[i][j])
            # rows
            for r in range(row, row+3):
                if sum(grid[r][col:col+3]) != 15:
                    return 0
            
            #cols
            for c in range(col, col+3):
                if grid[row][c]+grid[row+1][c]+grid[row+2][c] != 15:
                    return 0
            
            #diags 
            r,c = row, col
            dSum = 0
            while r < row+3:
                dSum += grid[r][c]
                r, c = r+1, c+1
            if dSum != 15:
                return 0

            r,c = row, col+2
            dSum = 0
            while r < row+3:
                dSum += grid[r][c]
                r, c = r+1, c-1
            if dSum != 15:
                return 0
            return 1
        
        res = 0
        for r in range(rows-2):
            for c in range(cols-2):
                res += magic(r, c)
        return res