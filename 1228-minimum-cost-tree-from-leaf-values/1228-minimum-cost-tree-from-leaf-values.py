class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)        
        # the maximum leaf value in the subarray arr[i..j]
        maxv = [[0] * n for _ in range(n)]

        for i in range(n):
            m = arr[i]
            maxv[i][i] = m
            for j in range(i + 1, n):
                m = max(m, arr[j])
                maxv[i][j] = m
        print(maxv)

        # dp[i][j] = min internal cost for arr[i..j]
        INF = 10 ** 20
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best = INF
                for k in range(i, j): # split
                    cost = dp[i][k] + dp[k + 1][j] + maxv[i][k] * maxv[k + 1][j]
                    if cost < best:
                        best = cost
                dp[i][j] = best
        return dp[0][n - 1]
