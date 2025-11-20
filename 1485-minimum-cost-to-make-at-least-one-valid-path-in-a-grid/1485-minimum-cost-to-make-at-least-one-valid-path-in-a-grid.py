class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        INF = 10 ** 10
        dist = [[INF] * cols for _ in range(rows)]
        dist[0][0] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(0, 0, 0)] # (cost, r, c)

        while pq:
            cost, r, c = heapq.heappop(pq)

            if r == rows - 1 and c == cols - 1:
                return cost

            for idx, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    flip = 0 if grid[r][c] == idx + 1 else 1
                    new_cost = cost + flip
                    
                    if dist[nr][nc] > new_cost:
                        dist[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))


                        
        return -1


            
            