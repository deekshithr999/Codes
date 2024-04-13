class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        c = set()
        nDiag = set()
        pDiag = set()

        #ndiag (row-col)# remains constant
        #pDiag (row+col)# remains constant
        def backTracking(row):
            if row == n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                if col in c or (row-col) in nDiag or (row+col) in pDiag:
                    continue
                c.add(col)
                nDiag.add(row-col)
                pDiag.add(row+col)
                backTracking(row+1)
                c.remove(col)
                nDiag.remove(row-col)
                pDiag.remove(row+col)
        backTracking(0)
        return res



class Solution:
    def totalNQueens(self, n: int) -> int:
        mat = [[0]*n for _ in range(n)]

        def checkInLeftDiag(currPos, mat):
            r,c = currPos
            while r>=0 and c >=0:
                if mat[r][c] :
                    return False
                r,c = r-1, c-1
            return True
        
        def checkInRightDiag(currPos, mat):
            r,c = currPos
            while r>=0 and c<n:
                if mat[r][c]:
                    return False
                r, c = r-1, c+1
            return  True
        
        def checkLinear(currPos, mat):
            r,c = currPos
            while r>=0 :
                if mat[r][c]:
                    return False
                r -= 1
            return True

        def arrangeQueens(currRow, mat):
            if currRow == n:
                return 1
            tot = 0
            for i in range(n):
                if not ( checkInLeftDiag((currRow, i), mat) and checkInRightDiag((currRow, i), mat) and checkLinear((currRow, i), mat ) ):
                    continue
                mat[currRow][i]=1
                tot += arrangeQueens(currRow+1, mat)
                mat[currRow][i]=0
            return tot

        return arrangeQueens(0, mat)
                
        