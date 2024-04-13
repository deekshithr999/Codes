class Solution:
    '''
    Unbounded knapsack Approach
    TC: O(m*n) # #ofcoins*amount
    SC: O(m*n)

    Can do better in terms of space complexity
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        
        ncoins = len(coins)
        dp = [[0]*(amount+1)]*(ncoins+1)
        for i in range(ncoins+1):
            dp[i][0]=1
        for i in range(ncoins):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[ncoins][amount]
        

class Solution:
    '''
    Memoization : 
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        res = 0
        def dfs(currIdx, remAmnt):
            if remAmnt < 0:
                return 0
            if remAmnt == 0:
                return 1

            if (currIdx, remAmnt) in cache:
                return cache[(currIdx, remAmnt)]

            nWays = 0
            for i in range(currIdx, len(coins)):
                nWays += dfs(i, remAmnt-coins[i])
            cache[(currIdx, remAmnt)] = nWays
            return nWays
        return dfs(0, amount)