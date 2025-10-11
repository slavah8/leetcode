class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        # dp[:i] defined as min cost to reach ith step
        # relation : dp[i] = min(dp[i - 1] +  dp[i - 2] dp[i - 3]
        N = len(costs)
        INF = 10 ** 10
        dp = [INF] * (N + 1)

        dp[0] = 0

        for i in range(1, N + 1):
            first = costs[i - 1] + (i - (i - 1)) ** 2 + (dp[i - 1] if i - 1 >= 0 else 0)
            second = costs[i - 1] + (i - (i - 2)) ** 2 + (dp[i - 2] if i - 2 >= 0 else 0)
            third = costs[i - 1] + (i - (i - 3)) ** 2 + (dp[i - 3] if i - 3 >= 0 else 0)
            dp[i] = min(first, second, third)
        
        return dp[N]