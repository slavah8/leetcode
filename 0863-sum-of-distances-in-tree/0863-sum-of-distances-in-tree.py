class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # cnt[v] = how many nodes in v’s subtree
        cnt = [1] * n
        
        # down[v] = total distance from v to nodes below it
        down = [0] * n


        # post order : children -> parent

        def dfs1(u, p):
            for v in graph[u]:
                if v == p:
                    continue
                dfs1(v, u)
                cnt[u] += cnt[v]
                # For all nodes inside v’s subtree, every distance from v grows by +1 when measured from u. 
                # There are cnt[v] such nodes.  
                down[u] += down[v] + cnt[v]


        # We “move” the root from a parent u to its child v. That shift changes distances
        # All nodes inside v’s subtree (there are cnt[v] of them) become 1 step closer to v.
        # → total sum decreases by cnt[v].
        # All nodes outside v’s subtree (there are n - cnt[v]) become 1 step farther from v.
        # → total sum increases by n - cnt[v]
        ans = [0] * n
        def dfs2(u, p):
            for v in graph[u]:
                if v == p:
                    continue
                ans[v] = ans[u] - cnt[v] + (n - cnt[v])
                dfs2(v, u)
        
        dfs1(0, -1)
        ans[0] = down[0]
        dfs2(0, -1)

        return ans
