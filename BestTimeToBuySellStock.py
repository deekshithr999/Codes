

'''
Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104


Sol 1:

get the diff for each current day and future days
Time Complexity :O(n^2)
space Complexity:O(1)
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        """
        max_profit =0
        for i in range(0,len(prices)-1):
            
            for j in range(i+1,len(prices)):
                
                profit=prices[j]-prices[i]
                max_profit=max(max_profit,profit)
        
        return max_profit

'''
Sol 2 :

subtract the current element from the minimum element present in the left array
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini=prices[0]
        max_profit=0
        for curr in prices:
            max_profit=max(max_profit,curr-mini)
            mini=min(mini,curr)
        
        return max_profit

'''
Sol 3:

traverse the array if the element is <min make it min else subract to 
get the profit
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minimum=prices[0]
        profit=0
        
        for i in range(0,len(prices)):
            
            if prices[i]<minimum:
                minimum=prices[i]
            
            else:
                profit =max(profit,prices[i]-minimum)
        
        return profit
        
            
        