class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = 3 * n
        pix = [[0] * size for _ in range(size)]

        for r in range(n):
            for c in range(n):
                ch = grid[r][c]
                nr, nc = 3 * r, 3 * c
                if ch == '/':
                    pix[nr][nc + 2] = 1
                    pix[nr + 1][nc + 1] = 1
                    pix[nr + 2][nc] = 1
                elif ch == '\\':
                    pix[nr][nc] = 1
                    pix[nr + 1][nc + 1] = 1
                    pix[nr + 2][nc + 2] = 1
        
        
        visited = [[False] * size for _ in range(size)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if visited[r][c]:
                return

            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < size and 0 <= nc < size and visited[nr][nc] == False and pix[nr][nc] == 0:
                    dfs(nr, nc)
    
        
        count = 0
        for r in range(size):
            for c in range(size):
                if pix[r][c] == 0 and not visited[r][c]:
                    dfs(r, c)
                    count += 1
        return count