class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        
        # dp[i][b] defined as max profit you can make for the first i stocks with b budget left
        n = len(present)
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            cost = present[i - 1]
            gain = future[i - 1] - cost
            if gain < 0:
                gain = 0
            
            for b in range(budget + 1):
                # skip this stock
                dp[i][b] = dp[i - 1][b]

                # take this stock
                if b >= cost and gain > 0:
                    dp[i][b] = max(dp[i][b], gain + dp[i - 1][b - cost])
        
        return dp[n][budget]
