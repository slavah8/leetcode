class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        ans = [0] * n
        # compute ans[0]
        def dfs1(u, parent):
            for v, w in graph[u]:
                if v == parent:
                    continue
                ans[0] += w
                dfs1(v, u)

        dfs1(0, -1)
        print(ans)
        def dfs_reroot(u, parent):
            for v, w in graph[u]:
                if v == parent:
                    continue
                
                if w == 0:
                    ans[v] = ans[u] + 1
                elif w == 1:
                    ans[v] = ans[u] - 1
                dfs_reroot(v, u)


        dfs_reroot(0, -1)
        return ans
