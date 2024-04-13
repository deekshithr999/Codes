class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        dt = {} # (i, buy)
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dt:
                return dt[(i, canBuy)]
            if canBuy:
                b = dfs(i+1, False) - prices[i]
                c = dfs(i+1, canBuy)
                dt [(i, canBuy)] = max(b,c)
            else:
                s = dfs(i+2, True) + prices[i]
                c = dfs(i+1, canBuy)
                dt [(i, canBuy)] = max(s,c)
            return dt[(i, canBuy)]
        return dfs(0, True)

        


class Solution:
    '''
    TC: O(n^2)
    SC: O(n)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        dpProfit = [0]*len(prices)
    
        for i in range(len(prices)-2, -1, -1):
            for j in range(i+1, len(prices)):
                dpProfit[i] = max(dpProfit[i],dpProfit[i+1], prices[j]-prices[i] + dpProfit[min(j+2, len(prices)-1)]) # can change this lamba code
        return dpProfit[0]        