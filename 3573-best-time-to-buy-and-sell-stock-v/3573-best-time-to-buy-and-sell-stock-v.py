class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        INF = 10 ** 10
        # dp[i][t][s] = max profit up to day i (0..i), using at most t transactions, and being in state s
        dp = [[[-INF] * 3 for _ in range(k + 1)] for _ in range(n)]

        # day 0 base case
        for t in range(k + 1):
            dp[0][t][0] = 0  # IMPORTANT: can always do nothing
            if t >= 1:
                dp[0][t][1] = -prices[0] #  # open long: buy
                dp[0][t][2] = prices[0] # short sell
        

        for i in range(1, n):
            p = prices[i]

            for t in range(k + 1):

                
                dp[i][t][0] = max(dp[i - 1][t][0], dp[i - 1][t][1] + p, dp[i - 1][t][2] - p)

                # normal transaction
                dp[i][t][1] = dp[i - 1][t][1]
                if t >= 1:
                    dp[i][t][1] = max(dp[i][t][1], dp[i - 1][t - 1][0] - p)
                
                # short transaction
                dp[i][t][2] = dp[i - 1][t][2]
                if t >= 1:
                    dp[i][t][2] = max(dp[i][t][2], dp[i - 1][t - 1][0] + p)

        return dp[n - 1][k][0]




