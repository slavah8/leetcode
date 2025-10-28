class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        INF = 10 ** 15
        # mask nodes visited
        # dp(mask, last_node) max cost with this mask and last_node visited
        graph = defaultdict(list)
        for u, v, cost in highways:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        FULL = (1 << n) - 1
        @lru_cache(None)
        def dfs(mask, last_node):
            steps = mask.bit_count() - 1
            if steps == k:
                return 0
            best = -INF
            for nei, cost in graph[last_node]:
                if mask & (1 << nei): # cant revisit cities
                    continue
                cand = cost + dfs(mask | (1 << nei), nei)
                if cand > best:
                    best = cand
            return best

     
        ans = -1
        for start in range(n):
            ans = max(ans, dfs(1 << start, start))
        return ans

            