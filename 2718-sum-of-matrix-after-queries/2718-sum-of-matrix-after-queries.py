class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        seen_cols = set()
        seen_rows = set()

        total = 0

        for typ, idx, val in reversed(queries):

            if typ == 0:
                # row 
                if idx in seen_rows:
                    continue
                
                total += val * (n - len(seen_cols))
                seen_rows.add(idx)
            
            if typ == 1:
                # col
                if idx in seen_cols:
                    continue
                
                total += val * (n - len(seen_rows))
                seen_cols.add(idx)
        
        return total