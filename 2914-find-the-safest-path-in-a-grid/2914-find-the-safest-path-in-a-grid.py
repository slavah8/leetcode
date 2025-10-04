class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dist = [[-1] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        # check if we can reach bottom right (r - 1, c - 1) with safety score >= S
        def can(dist, S):
            N = len(dist)
            if dist[0][0] < S:
                return False
            seen = [[False] * N for _ in range(N)]
            seen[0][0] = True
            queue = deque([(0, 0)])
            while queue:
                r, c = queue.popleft()
                if r == N - 1 and c == N - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and seen[nr][nc] == False and dist[nr][nc] >= S:
                        seen[nr][nc] = True
                        queue.append((nr, nc))
                
            return False

        # we want the highest safety possible
        N = len(grid)
        low = 0 
        high = 2 * (N - 1)

        while low < high:
            mid = (low + high + 1) // 2
            if can(dist, mid):
                low = mid
            else:
                high = mid - 1

        return low



        