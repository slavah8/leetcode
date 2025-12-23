class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)

        dp = [1] * (n + 1)
        seen = {}
        best = 1

        for i in range(n):
            x = arr[i]
            need = x - difference

            if need in seen:
                idx = seen[need]
                dp[i] = max(dp[i], 1 + dp[idx])
            
            seen[x] = i
            best = max(best, dp[i])
        return best

