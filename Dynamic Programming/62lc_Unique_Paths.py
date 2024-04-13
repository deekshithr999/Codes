class Solution:
    '''
    TC: O(n^2)
    SC: O(n^2)
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if j-1 >=0:
                    dp[i][j] = dp[i][j-1]
                if i-1 >=0:
                    dp[i][j]+=dp[i-1][j]
        return dp[m-1][n-1]
        