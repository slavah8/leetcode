class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        
        # build adj list
        N = len(parent)

        graph = [[] * N for _ in range(N)]

        for i in range(1, N):
            p = parent[i]
            graph[p].append(i)
        
        print(graph)

        # for every node u, the parity of letters on the path from the root to u
        masks = [0] * N

        def dfs(u):
            for v in graph[u]:
                bit = 1 << (ord(s[v]) - 97)
                masks[v] = masks[u] ^ bit
                dfs(v)
        
        dfs(0)

        cnt = defaultdict(int) # how many of these masks we have
        ans = 0
        for m in masks:
            # XOR = 0
            ans += cnt[m]

            # XOR has exactly one bit set
            for b in range(26):
                new_mask = (1 << b) ^ m
                ans += cnt[new_mask]
            
            cnt[m] += 1
        
        return ans


