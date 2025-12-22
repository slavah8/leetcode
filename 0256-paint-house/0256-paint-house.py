class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        # dp[i][j] defined as min cost to paint all houses up to i ending with color j
        INF = 10 ** 15
        n = len(costs)
        colors = 3
        dp = [[INF] * colors for _ in range(n)]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1, n):

            # red house
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]

            # blue house
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]

            # green house
            dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + costs[i][2]

        return min(dp[n - 1])