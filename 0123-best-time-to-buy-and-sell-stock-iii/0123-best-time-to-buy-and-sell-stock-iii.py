class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # dp[i][k][0] = max profit up to day i if you have completed k transactions and do NOT hold stock
        # dp[i][k][1] = max profit up to day i if you have completed k transactions and DO hold stock

        INF = 10 ** 10

        buy1 = -INF # buy1 = best profit after you’ve bought the 1st stock (so you’re holding 1 share)
        sell1 = 0 # sell1 = best profit after you’ve sold the 1st stock (0 share, completed 1 transaction)
        buy2 = -INF # best profit after second buy (holding 1 stock again)
        sell2 = 0 # best profit after second sell (holding 0 stock again)

        for p in prices:

            buy1 = max(buy1, -p)
            sell1 = max(sell1, p + buy1)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, p + buy2)
        
        return sell2

