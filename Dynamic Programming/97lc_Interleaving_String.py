
class Solution:
    '''
    DP: Using Matrix Method
    TC: O(n*m)
    SC: O(n*m)
    '''
    def isInterleave(self, X: str, Y: str, Z: str) -> bool:
        lx, ly, lz = len(X), len(Y), len(Z)
        if lx + ly != lz:
            return False
        dp = [[0]*(ly+1) for _ in range(lx+1)]
        dp[0][0] = True
        #rowwise
        for r in range(1, lx+1):
            if X[r-1] == Z[r-1]:
                dp[r][0] = dp[r-1][0]
        #columnwise
        for c in range(1, ly+1):
            if Y[c-1] == Z[c-1]:
                dp[0][c] = dp[0][c-1]
        #between
        for r in range(1, lx+1):
            for c in range(1, ly+1):
                if Z[r+c-1] == X[r-1]:
                    dp[r][c] = dp[r-1][c]
                if Z[r+c-1] == Y[c-1]:
                    dp[r][c] |= dp[r][c-1]
        
        return dp[lx][ly]



class Solution:
    '''
    Memoization
    TC: O(n*m)
    SC: O(n*m)
    '''
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i1, i2, i3):
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            if i3 == len(s3):
                if i1 == len(s1) and i2 == len(s2):
                    return True
                else:
                    return False

            tres = False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                tres |= dfs(i1+1, i2, i3+1)
            if i2 < len(s2) and s2[i2] == s3[i3]:
                tres |= dfs(i1, i2+1, i3+1)
            dp[(i1, i2)] = tres
            return dp[(i1, i2)]
        return dfs(0, 0, 0) 

