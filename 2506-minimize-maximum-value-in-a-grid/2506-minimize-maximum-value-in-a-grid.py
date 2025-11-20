class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        total = rows * cols

        # map r, c to a node (1 value)
        def mapping(r, c):
            return r * cols + c
        
        graph = defaultdict(list)
        deg = [0] * total

        for r in range(rows):
            cells = [] # (value, id)
            for c in range(cols):
                cells.append((grid[r][c], mapping(r, c)))
        
            cells.sort()
            # add edges from smaller to next larger val in this row
            for i in range(len(cells) - 1):
                u = cells[i][1]
                v = cells[i + 1][1]

                graph[u].append(v)
                deg[v] += 1
            
        
        # do the same for the columns dependencies
        for c in range(cols):
            cells = []
            for r in range(rows):
                cells.append((grid[r][c], mapping(r, c)))
            
            cells.sort()
            for i in range(len(cells) - 1):
                u = cells[i][1]
                v = cells[i + 1][1]

                graph[u].append(v)
                deg[v] += 1
        
        q = deque()
        print(graph)
        for u in range(total):
            if deg[u] == 0:
                q.append(u)
        
        val = [1] * total
        while q:
            u = q.popleft()
            for v in graph[u]:
                if val[v] < val[u] + 1:
                    val[v] = val[u] + 1
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        ans = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                ans[r][c] = val[mapping(r, c)]
        
        
        return ans
