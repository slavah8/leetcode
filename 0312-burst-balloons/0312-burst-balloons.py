class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]
        N = len(a)

        # max coins you can get by bursting all balloons from val[i:j]
        dp = [[0] * N for _ in range(N)]
        
        for length in range(2, N):
            for L in range(N - length):
                R = L + length
                best = 0
                for k in range(L + 1, R):
                    # if you burst k as the last balloon you get 
                    best = max(best, dp[L][k] + dp[k][R] + (a[L] * a[k] * a[R]))
                dp[L][R] = best
        
        return dp[0][N - 1]
