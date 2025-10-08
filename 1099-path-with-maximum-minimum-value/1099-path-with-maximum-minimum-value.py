class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # can we reach the bottom right grid with value greater than or equal to T
        def reachable(T):

            start = grid[0][0]
            if start < T:
                return False
            
            queue = deque()
            queue.append((0, 0))
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] >= T and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            
            return False
        
        low = 0
        maxx = 0
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val > maxx:
                    maxx = val
        high = maxx

        while low < high:
            mid = (low + high + 1) // 2
            if reachable(mid):
                low = mid
            else:
                high = mid - 1
        return low


