class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        deg = [0] * (n + 1)
        pair_count = defaultdict(int)

        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            pair_count[(u, v)] += 1

        sorted_deg = sorted(deg[1:])
        m = len(queries)
        ans = [0] * m
        print(sorted_deg)
        for idx, q in enumerate(queries):
            total = 0
            i = 0
            j = n - 1
            while i < j:
                if sorted_deg[i] + sorted_deg[j] <= q:
                    i += 1
                else:
                    total += (j - i)
                    j -= 1
            ans[idx] = total
        print(ans)


        for (u, v), c in pair_count.items():
            s = deg[u] + deg[v]
            for idx, q in enumerate(queries):
                if s > q and s - c <= q:
                    ans[idx] -= 1
        return ans

            
            