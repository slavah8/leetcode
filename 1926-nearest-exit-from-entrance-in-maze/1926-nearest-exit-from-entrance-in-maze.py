class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        rows = len(maze)
        cols = len(maze[0])
        start_r, start_c = entrance
        queue = deque([(start_r, start_c, 0, True)])
        visited = [[False] * cols for _ in range(rows)]
        visited[start_r][start_c] = True

        while queue:
            r, c, steps, is_entrance = queue.popleft()
            if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and not is_entrance:
                return steps
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maze[nr][nc] == '.':
                    queue.append((nr, nc, steps + 1, False))
                    visited[nr][nc] = True
        return -1



        