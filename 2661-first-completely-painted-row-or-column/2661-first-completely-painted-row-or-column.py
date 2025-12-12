class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        rows = len(mat)
        cols = len(mat[0])

        pos = {}

        for r in range(rows):
            for c in range(cols):
                val = mat[r][c]
                pos[val] = (r, c)
        
        print(pos)
        row_counts = [0] * rows
        col_counts = [0] * cols

        for i, val in enumerate(arr):
            r, c = pos[val]
            row_counts[r] += 1
            col_counts[c] += 1
            if row_counts[r] == cols:
                return i
            if col_counts[c] == rows:
                return i
