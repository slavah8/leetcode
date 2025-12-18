class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        start_r = x
        start_c = y

        row_list = []

        for r in range(start_r, start_r + k):
            curr_row = []
            for c in range(start_c, start_c + k):
                curr_row.append(grid[r][c])

            row_list.append(curr_row)
        
        row_list.reverse()
        print(row_list)

        for r in range(rows):
            for c in range(cols):
                if r == start_r and c == start_c:
                    i = 0
                    while i < len(row_list):
                        grid[r][c: c + k] = row_list[i]
                        i += 1
                        r = r + 1
                
        return grid


