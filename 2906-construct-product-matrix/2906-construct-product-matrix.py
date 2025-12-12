class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        MOD = 12345

        N = rows * cols
        a = [0] * N
        idx = 0
        for r in range(rows):
            for c in range(cols):
                x = grid[r][c]
                a[idx] = x
                idx += 1
        
        print(a)
        prefix = [1] * N
        pref = 1
        for i in range(N):
            prefix[i] = pref
            pref = (pref * a[i]) % MOD
        
        print(prefix)

        suffix = [1] * N
        suff = 1
        for i in range(N - 1, -1, -1):
            suffix[i] = suff
            suff = (suff * a[i]) % MOD
        
        print(suffix)

        ans = [1] * N
        for i in range(N):
            ans[i] = (prefix[i] * suffix[i]) % MOD
        
        p = [[0] * cols for _ in range(rows)]
        idx = 0
        for r in range(rows):
            for c in range(cols):
                p[r][c] = ans[idx]
                idx += 1
        return p