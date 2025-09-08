class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        

        def dfs_label(r, c, label):
            if r < 0 or r >= N or c < 0 or c >= N:
                return 0
            if grid[r][c] != 1:
                return 0

            grid[r][c] = label
            size = 1
            for dr, dc in directions:
                size += dfs_label(r + dr, c + dc, label)
            return size
        
        island_area = {}
        label = 2
        has_zero = False

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    has_zero = True
                elif grid[r][c] == 1:
                    area = dfs_label(r, c, label)
                    island_area[label] = area
                    label += 1

        if not has_zero:
            return N * N
        max_size = 1
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            neighbor_label = grid[nr][nc]
                            if neighbor_label > 1 and neighbor_label not in seen:
                                seen.add(neighbor_label)
                                size += island_area[neighbor_label]
                    max_size = max(max_size, size)
        
        return max_size
        