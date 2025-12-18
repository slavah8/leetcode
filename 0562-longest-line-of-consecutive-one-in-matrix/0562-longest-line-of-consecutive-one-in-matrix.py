class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        # dp[r][c][k] = longest line of 1s ending at (r,c) in direction k:
        dp = [[[0, 0, 0, 0] for _ in range(cols)] for _ in range(rows)]

        best = 0

        for r in range(rows):
            for c in range(cols):

                if mat[r][c] == 1:

                    # horizontal
                    dp[r][c][0] = 1 + (dp[r][c - 1][0] if c - 1 >= 0 else 0)

                    # vertical
                    dp[r][c][1] = 1 + (dp[r - 1][c][1] if r - 1 >= 0 else 0)

                    # diagonal
                    dp[r][c][2] = 1 + (dp[r - 1][c - 1][2] if r - 1 >= 0 and c - 1 >= 0 else 0)

                    # anti
                    dp[r][c][3] = 1 + (dp[r - 1][c + 1][3] if r - 1 >= 0 and c + 1 < cols else 0)

                    best = max(best, dp[r][c][0], dp[r][c][1], dp[r][c][2], dp[r][c][3])
        
        return best