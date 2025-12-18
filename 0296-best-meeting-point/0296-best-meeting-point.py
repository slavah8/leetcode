class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        row_list = []
        col_list = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_list.append(r)
                    col_list.append(c)
        
        row_list.sort()
        col_list.sort()
        print(row_list)
        print(col_list)

        mr = row_list[len(row_list) // 2]
        mc = col_list[len(col_list) // 2]

        ans = 0 
        for r in row_list:
            ans += abs(r - mr)
        
        for c in col_list:
            ans += abs(c - mc)
        
        return ans
        