class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        
        # dp[i][points] ways to score number of points after solving the first i types
        MOD = 10 ** 9 + 7
        N = len(types)
        dp = [[0] * (target + 1) for _ in range(N + 1)]

        dp[0][0] = 1
        
        for i in range(1, N + 1):
            count, points = types[i - 1]
            
            for t in range(0, target + 1):
                total = dp[i - 1][t]
                min_c = min(count, t // points)
                for c in range(1, min_c + 1):
                    total += (dp[i - 1][t - (c * points)]) % MOD
                dp[i][t] = total
    

        
        return dp[N][target] % MOD


                                