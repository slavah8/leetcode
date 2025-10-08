class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # dp[i] = max subarray sum up to index i with one deletion
        N = len(arr)
        INF = 10 ** 10
        dp0 = [0] * N  # best sum ending at i with no deletion
        dp1 = [0] * N # best sum ending at i with exactly one deletion
        dp0[0] = arr[0]
        dp1[0] = -INF
        
        best = dp0[0]
        for i in range(1, N):
            x = arr[i]
            dp0[i] = max(x, dp0[i - 1] + x) # start new or continue 
            dp1[i] = max(dp0[i - 1], dp1[i - 1] + x)
            best = max(best, dp0[i], dp1[i])
        return best
