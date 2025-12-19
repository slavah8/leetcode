class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        
        rows = len(grid)
        cols = len(grid[0])
        
        # dp[r][c][k] = True if there exists a path from (0,0) to (r,c) that uses exactly k ones.
        L = rows + cols - 1
        if L % 2 == 1:
            return False
        
        need = L // 2

        dp = [[[False] * (L + 1) for _ in range(cols)] for _ in range(rows)]
        dp[0][0][grid[0][0]] = True

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                v = grid[r][c]
                max_k = r + c + 1

                for k in range(0, max_k + 1):
                    k_prev = k - v
                    if k_prev < 0:
                        continue
                    
                    ok = False
                    if r > 0 and dp[r - 1][c][k_prev]:
                        ok = True
                    if c > 0 and dp[r][c - 1][k_prev]:
                        ok = True
                    dp[r][c][k] = ok
        return dp[rows - 1][cols - 1][need]