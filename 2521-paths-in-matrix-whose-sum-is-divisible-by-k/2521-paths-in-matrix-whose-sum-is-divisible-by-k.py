from typing import List
from functools import cache

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        M, N = len(grid), len(grid[0])
        # # prev[j][r] = number of ways to reach cell (i-1, j) with remainder r
        # prev[j][r] = previous row 

        for i in range(M): # go row by row only needed the row above it for calculation (rolling)
            # curr[j][r] = curr row
            # Build curr[j][r] for the current row, using prev[j] (up) and curr[j-1] (left).
            curr = [[0] * k for _ in range(N)]
            for j in range(N):
                val = grid[i][j] % k

                if i == 0 and j == 0:
                    curr[0][val] = 1
                    continue
                
                # from UP (i - 1, j) -> (i, j)
                if i > 0:
                    up = prev[j]
                    for r in range(k):
                        nr = (val + r) % k
                        curr[j][nr] = (curr[j][nr] + up[r]) % MOD
                    
                # from LEFT (i, j - 1) -> (i, j)
                if j > 0:
                    left = curr[j - 1]
                    for r in range(k):
                        nr = (val + r) % k
                        curr[j][nr] = (curr[j][nr] + left[r]) % MOD
            prev = curr
        
        return prev[N - 1][0] % MOD

        