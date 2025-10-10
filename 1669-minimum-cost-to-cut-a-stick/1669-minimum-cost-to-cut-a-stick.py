class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        # dp[i][j] min cost to fully cut (pts[i], pts[j])

        pts = [0] + sorted(cuts) + [n]
        m = len(pts)
        dp = [[0] * m for _ in range(m)]
        INF = 10 ** 20
        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                best = INF
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + (pts[j] - pts[i])
                    if cost < best:
                        best = cost
                dp[i][j] = 0 if best == INF else best
        
        return dp[0][m - 1]