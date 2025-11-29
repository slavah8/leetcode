class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        rows = len(image)
        cols = len(image[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        min_row = x
        max_row = x
        min_col = y
        max_col = y
        visited = [[False] * cols for _ in range(rows)]
        def dfs(r, c):
            nonlocal min_row, max_row, min_col, max_col

            visited[r][c] = True
            if r < min_row:
                min_row = r
            if r > max_row:
                max_row = r
            
            if c < min_col:
                min_col = c
            if c > max_col:
                max_col = c

            for dr, dc in directions:
                nr, nc = dr + r, dc + c 
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == '1' and not visited[nr][nc]:
                    dfs(nr, nc)

        dfs(x, y)
        print(min_row, max_row)
        print(min_col, max_col)
        return (max_row - min_row + 1) * (max_col - min_col + 1)

