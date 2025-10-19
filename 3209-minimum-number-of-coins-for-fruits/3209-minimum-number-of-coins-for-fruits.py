class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        INF = 10 ** 15
        # dp[t] defined as minimum number of coins to acquire fruits 1...t 
        dp = [INF] * (n + 1)
        dp[0] = 0

        for t in range(1, n + 1):
            # j represents the index of the last fruit you actually buy when acquiring fruits 1..t
            # if i buy j then i cover min(2j, n)
            # You can’t buy after the goal fruit → j ≤ t
            # Your free coverage from that purchase must reach fruit t → t ≤ 2j -> t / 2 <= j
            # range for j [t / 2, t]
            low = math.ceil(t / 2)
            high = t
            for j in range(low, high + 1):
                # if i buy fruit j then i need dp[j - 1] + prices[j]
                dp[t] = min(dp[t], dp[j - 1] + prices[j - 1])
            
        return dp[n]

