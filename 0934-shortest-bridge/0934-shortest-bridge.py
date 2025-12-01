class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        INF = 10 ** 10
        queue = deque()
        
        def dfs(r, c):
            grid[r][c] = 2
            queue.append((r, c, 0))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        found = False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
        
        
        visited = [[False] * cols for _ in range(rows)]
        
        for r, c, _ in queue:
            visited[r][c] = True
        
        while queue:
            r, c, d = queue.popleft()
            if grid[r][c] == 1:
                return d - 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 2 and not visited[nr][nc]:
                    queue.append((nr, nc, d + 1))
                    visited[nr][nc] = True


        
        
        



