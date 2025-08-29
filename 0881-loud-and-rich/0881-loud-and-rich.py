class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        answer = [-1] * N
        graph = collections.defaultdict(list) # who's richer than this node?
        indegree = [0] * N
        for u, v in richer:
            # u is richer than v
            graph[v].append(u)

        print(graph)
        INF = 10 ** 10

        @lru_cache(maxsize=None)
        def dfs(node):

            min_quiet = (quiet[node], node)

            for neighbor in graph[node]:
                if neighbor != node:
                    neighbor_quiet, neighbor_node = dfs(neighbor)
                    if neighbor_quiet < min_quiet[0]:
                        min_quiet = (neighbor_quiet, neighbor_node)
            return min_quiet
        
        for node in range(N):
            answer[node] = dfs(node)[1]
        
        return answer

                
