class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        n = len(values)
        dp = [[0] * n for _ in range(n)] # minimum total score to triangulate the polygonal chain from vertex i to vertex j
        INF = 10 ** 20
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best = INF
                for k in range(i + 1, j): # pick split at vertice k
                    cost = (values[i] * values[k] * values[j]) + dp[i][k] + dp[k][j]
                    if cost < best:
                        best = cost
                dp[i][j] = best
        
        return dp[0][n - 1]
