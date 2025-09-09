class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = collections.defaultdict(list)
        for (u, v), w in zip(equations, values):
            graph[u].append((v, w))
            graph[v].append((u, 1 / w))
        print(graph)

        def dfs(node, end, cur_weight):
            nonlocal visited

            if node == end:
                return cur_weight
            
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    res = dfs(neighbor, end, cur_weight * weight)
                    if res != -1:
                        return res

            return -1 # cant find end


        N = len(queries)
        answer = [-1] * N
        for i, (start, end) in enumerate(queries):
            visited = set()
            if end not in graph or start not in graph:
                answer[i] = -1
            else:
                answer[i] = dfs(start, end, 1)
        
        return answer