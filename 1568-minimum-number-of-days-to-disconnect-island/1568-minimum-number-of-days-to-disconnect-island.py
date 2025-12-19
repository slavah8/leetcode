class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    dfs(nr, nc, visited)

        
        def count_islands():

            visited = [[False] * cols for _ in range(rows)]
            islands = 0
            for r in range(rows):
                for c in range(cols):
                    if not visited[r][c] and grid[r][c] == 1:
                        visited[r][c] = True
                        islands += 1
                        dfs(r, c, visited)
            return islands
        
        if count_islands() != 1:
            return 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if count_islands() != 1:
                        return 1
                    grid[r][c] = 1
        
        return 2
            

