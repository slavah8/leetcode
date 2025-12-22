class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # dp[j] = length of the longest "valid kept columns" subsequence ending at column j
        m = len(strs[0])
        n = len(strs)
        dp = [1] * m
        best = 1
        for j in range(m):
            for i in range(j):
                ok = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], 1 + dp[i])
            best = max(best, dp[j])
        return m - best