
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down Approach
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]= min(dp[a], dp[a-c]+1)
        return dp[amount] if dp[amount] != (amount+1) else -1

        

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom up approach
        
        dp=[-1]*(amount+1)
        dp[0]=0

        def findChange(amnt):
            if dp[amnt]!= -1:
                # print("cmng here")
                return dp[amnt]
            else:
                tot_coins = float('inf')
                for coin in coins:
                    rem_amnt = amnt - coin
                    if rem_amnt <0:
                        continue
                    tot_coins =  min(findChange(rem_amnt)+1, tot_coins)
                    # print("tot coins ", tot_coins)
                dp[amnt]= tot_coins
                return dp[amnt]
        ret_val = findChange(amount)
        if ret_val == float('inf'):
            return -1
        return ret_val

        