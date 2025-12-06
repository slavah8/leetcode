class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[i][j] defined as max profit up to prices[:i] either buying or holding a stock at that time
        # j = 0 if you are not holding a stock
        # j = 1 if you are holding a stock
        
        dp = [[0] * 2 for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        best = 0
        for i in range(1, n):
            # not holding
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + (prices[i] - fee))

            # holding
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

            best = max(dp[i][0], dp[i][1], best)
        
        print(dp)
        return best




            