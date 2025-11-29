class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        
        rows = len(mat)
        cols = len(mat[0])

        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append((mat[r][c], r, c))
        
        cells.sort(key = lambda x: x[0])

        row_best = [0] * rows
        col_best = [0] * cols
        i = 0
        n = len(cells)
        ans = 0

        while i < n:

            j = i
            v = cells[i][0]
            while j < n and cells[j][0] == v:
                j += 1
            
            temp = []
            for k in range(i, j):
                _, r, c = cells[k]
                best_before = max(row_best[r], col_best[c])
                dp_val = best_before + 1
                temp.append((r, c, dp_val))
                ans = max(ans, dp_val)

            for r, c, dp_val in temp:
                row_best[r] = max(dp_val, row_best[r])
                col_best[c] = max(dp_val, col_best[c])
            
            i = j
        return ans


