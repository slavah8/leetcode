class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = (2 ** 31) - 1

        rows = len(rooms)
        cols = len(rooms[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))
        print(queue)
        while queue:
            row, col, level = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = level + 1
                    queue.append((nr, nc, level + 1))
