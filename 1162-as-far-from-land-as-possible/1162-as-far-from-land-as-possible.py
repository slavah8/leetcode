class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]
        INF = 10 ** 10
        best = -INF
        land = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land += 1
                    queue.append((r, c, 0))
                    visited[r][c] = True
        
        if land == 0 or land == rows * cols:
            return -1
            
        while queue:
            r, c, d = queue.popleft()
            if d > best:
                best = d


            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    queue.append((nr, nc, d + 1))
                    visited[nr][nc] = True
        
        return best if best > -INF else -1
