class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        INF = 10 ** 10
        rows = len(maze)
        cols = len(maze[0])

        # dist[r][c] shortest dist to reach (r, c)
        dist = [[INF] * cols for _ in range(rows)]

        start_r, start_c = start
        dest_r, dest_c = destination
        dist[start_r][start_c] = 0

        pq = [(0, start_r, start_c)] # (dist, r, c)

        while pq:
            print(pq)
            d, r, c = heapq.heappop(pq)
            if r == dest_r and c == dest_c:
                return True
            

            
            # left, right, down, up : possible moves

            # left
            new_left = c
            while new_left - 1 >= 0 and maze[r][new_left - 1] == 0:
                new_left -= 1
            
            roll_left = abs(c - new_left)
            if roll_left + d < dist[r][new_left]:
                dist[r][new_left] = roll_left + d
                heapq.heappush(pq, (dist[r][new_left], r, new_left))

            # right
            new_right = c
            while new_right + 1 < cols and maze[r][new_right + 1] == 0:
                new_right += 1
            roll_right = abs(c - new_right)
            if roll_right + d < dist[r][new_right]:
                dist[r][new_right] = roll_right + d
                heapq.heappush(pq, (dist[r][new_right], r, new_right))

            # up 
            new_up = r
            while new_up - 1 >= 0 and maze[new_up - 1][c] == 0:
                new_up -= 1
            roll_up = abs(r - new_up)
            if roll_up + d < dist[new_up][c]:
                dist[new_up][c] = roll_up + d
                heapq.heappush(pq, (dist[new_up][c], new_up, c))

            # down
            new_down = r
            while new_down + 1 < rows and maze[new_down + 1][c] == 0:
                new_down += 1
            roll_down = abs(r - new_down)
            if roll_down + d < dist[new_down][c]:
                dist[new_down][c] = roll_down + d
                heapq.heappush(pq, (dist[new_down][c], new_down, c))
        return False