class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)

        # dp[i] = maximum sum we can get from the suffix starting at index i

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            best = 0
            mx = 0
            for length in range(1, k + 1):
                if i + length > n:
                    break
                mx = max(mx, arr[i + length - 1])

                best = max(best, mx * length + dp[i + length])
            
            dp[i] = best
        
        return dp[0]
                


