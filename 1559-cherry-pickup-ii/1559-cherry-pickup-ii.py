class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #  (i + 1, j + 1) diag down then right
        #  (i + 1, j - 1) diag down then left
        #  (i + 1, j) down

        rows = len(grid)
        cols = len(grid[0])
       
        # Let dp[r][c1][c2] = max cherries robots can collect starting at row r when
        # robot A is at column c1
        # robot B is at column c2
        INF = 10 ** 15
        # dp[c1][c2] = best from row r + 1 with robots at columns c1 and c2
        dp_next = [[-INF] * (cols) for _ in range(cols)] 

        for c1 in range(cols):
            for c2 in range(cols):
                if c1 == c2:
                    dp_next[c1][c2] = grid[rows - 1][c1]
                else:
                    dp_next[c1][c2] = grid[rows - 1][c1] + grid[rows - 1][c2]

        for r in range(rows - 2, -1, -1):
            dp_curr = [[-INF] * (cols) for _ in range(cols)] 
            for c1 in range(cols):
                for c2 in range(cols):
                    gain = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)

                    best_next = -INF
                    for dc1 in (-1, 0, 1):
                        nc1 = c1 + dc1
                        if not (0 <= nc1 < cols):
                            continue
                        for dc2 in (-1, 0, 1):
                            nc2 = c2 + dc2
                            if not (0 <= nc2 < cols):
                                continue
                            best_next = max(best_next, dp_next[nc1][nc2])
                    if best_next != -INF:
                        dp_curr[c1][c2] = best_next + gain
            
            dp_next = dp_curr
        

        return dp_next[0][cols - 1]




        




