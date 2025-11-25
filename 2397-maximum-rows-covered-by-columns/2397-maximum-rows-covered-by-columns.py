class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        
        best = 0
        rows = len(matrix)
        cols = len(matrix[0])
        if numSelect >= cols:
            return rows

        def check(columns):
            rows_covered = 0
            for r in range(rows):
                ok = True
                for c in range(cols):
                    if c in columns:
                        continue

                    if matrix[r][c] == 1:
                        ok = False
                        break
                if ok:
                    rows_covered += 1
            return rows_covered

        def backtrack(start, remaining, columns):
            nonlocal best
            if remaining == 0:
                cand = check(columns)
                if cand > best:
                    best = cand
                return
    

            # cover this column
            for c in range(start, cols):
                if c not in columns:
                    columns.add(c)
                    backtrack(c + 1, remaining - 1, columns)
                    columns.remove(c)
            
        backtrack(0, numSelect, set())
        return best