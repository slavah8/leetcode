class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            
            if r2 + 1 <= n:
                diff[r2 + 1][c1] -= 1
            if c2 + 1 <= n:
                diff[r1][c2 + 1] -= 1
            if r2 + 1 <= n and c2 + 1 <= n:
                diff[r2 + 1][c2 + 1] += 1
        
        for r in range(n): # left to right
            run = 0
            for c in range(n):
                run += diff[r][c]
                diff[r][c] = run
        
        for c in range(n): # top to bot
            run = 0
            for r in range(n):
                run += diff[r][c]
                diff[r][c] = run
        mat = [row[:n] for row in diff[:n]]
        return mat
            