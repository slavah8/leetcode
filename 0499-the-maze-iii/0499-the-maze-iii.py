class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        INF = 10 ** 10
        rows = len(maze)
        cols = len(maze[0])

        # dist[r][c] shortest dist to reach (r, c)
        dist = [[INF] * cols for _ in range(rows)]
        path_best = [[""] * cols for _ in range(rows)]

        start_r, start_c = ball
        dest_r, dest_c = hole
        dist[start_r][start_c] = 0

        pq = [(0, "", start_r, start_c)] # (dist, cur_path, r, c)

        while pq:
            print(pq)
            d, path, r, c = heapq.heappop(pq)

            # Skip stale states
            if d > dist[r][c] or (d == dist[r][c] and path > path_best[r][c]):
                continue

            if r == dest_r and c == dest_c:
                return path
            
            # left, right, down, up : possible moves

            # LEFT
            new_c = c
            steps = 0
            while new_c - 1 >= 0 and maze[r][new_c - 1] == 0:
                new_c -= 1
                steps += 1
                if r == dest_r and new_c == dest_c:
                    break
            nd = d + steps
            np = path + "l"
            if steps > 0 and (nd < dist[r][new_c] or (nd == dist[r][new_c] and np < path_best[r][new_c])):
                dist[r][new_c] = nd
                path_best[r][new_c] = np
                heapq.heappush(pq, (nd, np, r, new_c))

            # RIGHT
            new_c = c
            steps = 0
            while new_c + 1 < cols and maze[r][new_c + 1] == 0:
                new_c += 1
                steps += 1
                if r == dest_r and new_c == dest_c:
                    break
            nd = d + steps
            np = path + "r"
            if steps > 0 and (nd < dist[r][new_c] or (nd == dist[r][new_c] and np < path_best[r][new_c])):
                dist[r][new_c] = nd
                path_best[r][new_c] = np
                heapq.heappush(pq, (nd, np, r, new_c))

            # UP
            new_r = r
            steps = 0
            while new_r - 1 >= 0 and maze[new_r - 1][c] == 0:
                new_r -= 1
                steps += 1
                if new_r == dest_r and c == dest_c:
                    break
            nd = d + steps
            np = path + "u"
            if steps > 0 and (nd < dist[new_r][c] or (nd == dist[new_r][c] and np < path_best[new_r][c])):
                dist[new_r][c] = nd
                path_best[new_r][c] = np
                heapq.heappush(pq, (nd, np, new_r, c))

            # DOWN
            new_r = r
            steps = 0
            while new_r + 1 < rows and maze[new_r + 1][c] == 0:
                new_r += 1
                steps += 1
                if new_r == dest_r and c == dest_c:
                    break
            nd = d + steps
            np = path + "d"
            if steps > 0 and (nd < dist[new_r][c] or (nd == dist[new_r][c] and np < path_best[new_r][c])):
                dist[new_r][c] = nd
                path_best[new_r][c] = np
                heapq.heappush(pq, (nd, np, new_r, c))

        return "impossible"