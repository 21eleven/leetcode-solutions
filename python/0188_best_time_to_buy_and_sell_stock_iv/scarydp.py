"""
188. Best Time to Buy and Sell Stock IV
Hard

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

 

Constraints:

    0 <= k <= 109
    0 <= prices.length <= 104
    0 <= prices[i] <= 1000

"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if not prices or k==0:
            return 0
        
        if 2*k > n:
            res = 0
            for i in range(1,n):
                res += max(0, prices[i]-prices[i-1])
            return res
        
        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]
        
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        
        for i in range(1,n):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        res = max(dp[n-1][j][0] for j in range(k+1))
        return res
