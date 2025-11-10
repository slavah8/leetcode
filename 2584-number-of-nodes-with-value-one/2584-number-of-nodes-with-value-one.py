class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        
        flip_here = [0] * (n + 1)

        counts = Counter(queries)
        for v, cnt in counts.items():
            if cnt & 1:
                flip_here[v] = 1
        
        ans = 0
        
        print(flip_here)
        def dfs(node, parity):
            nonlocal ans

            parity ^= flip_here[node]
            if parity == 1:
                ans += 1

            left = node * 2
            right = node * 2 + 1
            
            if left <= n:
                dfs(left, parity)
            if right <= n:
                dfs(right, parity)
        
        dfs(1, 0)
        return ans

            