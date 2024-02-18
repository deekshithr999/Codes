class Solution:
    '''
    TC: O(n^2)
    SC: O(n)
    '''
    def numSquares(self, n: int) -> int:
        dp = [n+1]*(n+1)
        dp[0]=0

        for target in range(1, n+1):
            for s in range(1, target+1):
                square = s**2
                if target-square<0:
                    break
                dp[target]= min(dp[target], 1+dp[target-square])
        return dp[n]