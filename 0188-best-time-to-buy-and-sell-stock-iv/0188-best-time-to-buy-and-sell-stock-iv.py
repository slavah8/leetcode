class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        INF = 10 ** 10
        n = len(prices)
        # dp[i][t][0] = max profit up to day i after exactly t completed sells, not holding
        dp = [[[-INF, -INF] for _ in range(k + 1)] for _ in range(n)]


        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]


        for i in range(1, n):
            p = prices[i]

            for t in range(k + 1):

                # do nothing
                dp[i][t][0] = dp[i - 1][t][0]

                # sell today
                if t >= 1:
                    dp[i][t][0] = max(p + dp[i - 1][t - 1][1], dp[i][t][0])

                # hold today
                dp[i][t][1] = dp[i - 1][t][1]

                # buy today
                dp[i][t][1] = max(dp[i - 1][t][0] - p, dp[i][t][1])

        return max(dp[n - 1][t][0] for t in range(k + 1))




