class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        new_grid = [r[:] for r in grid]
        visited = [[False] * cols for _ in range(rows)]
        def dfs(r, c, initial_color):
            
            visited[r][c] = True
            if r - 1 < 0 or c - 1 < 0 or r + 1 >= rows or c + 1 >= cols:
                # boundary
                new_grid[r][c] = color
            
            border = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= rows or nc >= cols or nr < 0 or nc < 0 or grid[nr][nc] != initial_color:
                    new_grid[r][c] = color
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == initial_color:
                    dfs(nr, nc, initial_color)


        

        dfs(row, col, grid[row][col])
        return new_grid
    