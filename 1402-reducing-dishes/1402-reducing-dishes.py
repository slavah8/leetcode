class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        n = len(satisfaction)
        satisfaction.sort()
        # dp[i][t] maximum like-time score you can get using dishes from index i..n-1, if the next dish you cook will be at time t.
        dp = [[0] * (n + 2) for _ in range(n + 1)]


        for i in range(n - 1, -1, -1):

            for t in range(n, 0, -1):
                skip = dp[i + 1][t]

                take = (satisfaction[i] * t) + dp[i + 1][t + 1]

                dp[i][t] = max(skip, take)
        
        return dp[0][1]

