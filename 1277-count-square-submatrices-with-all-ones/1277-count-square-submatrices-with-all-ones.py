class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if c == 0 or r == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                
                    ans += dp[r][c]
        
        return ans
                
