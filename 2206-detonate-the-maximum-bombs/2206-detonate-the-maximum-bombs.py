class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)

        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, rj = bombs[j]
                dx = xj - xi
                dy = yj - yi
                if dx*dx + dy*dy <= ri*ri:
                    graph[i].append(j)
        
        print(graph)
                





        def dfs(bomb, visited):
            count = 1
            visited.add(bomb)
            for nei in graph[bomb]:
                if nei not in visited:
                    count += dfs(nei, visited)
        
            return count

        best = 0
        for node in range(n):
            visited = set()
            best = max(best, dfs(node, visited))
        return best
        

        