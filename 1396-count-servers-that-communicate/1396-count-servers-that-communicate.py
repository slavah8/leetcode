class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        
        pc_connection = collections.defaultdict(bool)
        col_to_row = collections.defaultdict(list)
        row_to_col = collections.defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_to_col[r].append(c)
                    col_to_row[c].append(r)
                    pc_connection[(r, c)]
        
        print(row_to_col)
        print(col_to_row)
        print(pc_connection)
        
        for r in row_to_col.keys():
            if len(row_to_col[r]) > 1:
                for c in row_to_col[r]:
                    pc_connection[(r, c)] = True
        print(pc_connection)

        for c in col_to_row.keys():
            if len(col_to_row[c]) > 1:
                for r in col_to_row[c]:
                    pc_connection[(r, c)] = True
        
        print(pc_connection)

        count = 0
        for _, boolean in pc_connection.items():
            if boolean == True:
                count += 1
        
        return count
                
        


