class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        directions = [
                    (2, 1), (1, 2), (-1, 2), (-2, 1),
                    (-2, -1), (-1, -2), (1, -2), (2, -1)
                ]

        dp = [[1.0] * n for _ in range(n)]

        for step in range(1, k + 1):
            new_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    prob = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            prob += dp[nr][nc] / 8.0
                    new_dp[r][c] = prob
            dp = new_dp
        
        return dp[row][column]
