class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        shapes = set()
        seen = [[False] * cols for _ in range(rows)]

        def dfs(r0, c0, r, c, offsets):
            seen[r][c] = True
            offsets.append((r - r0, c - c0))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not seen[nr][nc] and grid[nr][nc] == 1:
                    dfs(r0, c0, nr, nc, offsets)
            
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not seen[r][c]:
                    offsets = []
                    dfs(r, c, r, c, offsets)
                    shape = tuple(sorted(offsets))
                    shapes.add(shape)
        return len(shapes)
