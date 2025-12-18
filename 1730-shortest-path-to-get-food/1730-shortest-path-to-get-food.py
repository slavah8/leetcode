class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        queue = deque()
        visited = [[False] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '#':
                    queue.append((r, c, 0))
                    visited[r][c] = True
        
        print(queue)
        while queue:
            r, c, time = queue.popleft()

            if grid[r][c] == '*':
                return time
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X' and not visited[nr][nc]:
                    queue.append((nr, nc, time + 1))
                    visited[nr][nc] = True
        
        return -1
