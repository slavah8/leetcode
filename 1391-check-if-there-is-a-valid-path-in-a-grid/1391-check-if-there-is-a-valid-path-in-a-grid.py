class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        def dfs(r, c, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            print(r, c)
            if visited[r][c]:
                return False

            visited[r][c] = True

            if r == rows - 1 and c == cols - 1:
                return True
            direction = grid[r][c]

            if direction == 1: # right or left
                if c + 1 < cols:
                    nxt = grid[r][c + 1]
                    if nxt != 2 and nxt != 4 and nxt != 6:
                        if dfs(r, c + 1, direction):
                            return True
                if c - 1 >= 0:
                    nxt = grid[r][c - 1]
                    if nxt != 5 and nxt != 2 and nxt != 3:
                        if dfs(r, c - 1, direction):
                            return True

            elif direction == 2: # down or up
                if r + 1 < rows: # down
                    nxt = grid[r + 1][c]
                    if nxt != 4 and nxt != 3 and nxt != 1:
                        if dfs(r + 1, c, direction):
                            return True
                if r - 1 >= 0: # up
                    nxt = grid[r - 1][c]
                    if nxt != 5 and nxt != 6 and nxt != 1:
                        if dfs(r - 1, c, direction):
                            return True
        
            elif direction == 3: # go left or go down
                if r + 1 < rows: # down
                    nxt = grid[r + 1][c]
                    if nxt != 4 and nxt != 1 and nxt != 3:
                        if dfs(r + 1, c, direction):
                            return True
                if c - 1 >= 0:
                    nxt = grid[r][c - 1]
                    if nxt != 2 and nxt != 5 and nxt != 3:
                        if dfs(r, c - 1, direction):
                            return True
                     
            elif direction == 4: # go down or go right
                if c + 1 < cols: # go right
                    nxt = grid[r][c + 1]
                    if nxt != 2 and nxt != 6 and nxt != 4:
                        if dfs(r, c + 1, direction):
                            return True
                if r + 1 < rows:
                    nxt = grid[r + 1][c]
                    if nxt != 4 and nxt != 3 and nxt != 1:
                        if dfs(r + 1, c, direction):
                            return True

            elif direction == 5: # go left or go up
                if r - 1 >= 0: # up
                    nxt = grid[r - 1][c]
                    if nxt != 6 and nxt != 1 and nxt != 5:
                        if dfs(r - 1, c, direction):
                            return True
                if c - 1 >= 0: # left
                    nxt = grid[r][c - 1]
                    if nxt != 3 and nxt != 2 and nxt != 5:
                        if dfs(r, c - 1, direction):
                            return True
     
            elif direction == 6:
                if c + 1 < cols: # go right or up
                    nxt = grid[r][c + 1]
                    if nxt != 2 and nxt != 4 and nxt != 6:
                        if dfs(r, c + 1, direction):
                            return True
                if r - 1 >= 0:
                    nxt = grid[r - 1][c]
                    if nxt != 6 and nxt != 5 and nxt != 1:
                        if dfs(r - 1, c, direction):
                            return True
             
            return False

        return dfs(0, 0, -1)