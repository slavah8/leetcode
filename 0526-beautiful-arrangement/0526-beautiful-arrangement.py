class Solution:
    def countArrangement(self, n: int) -> int:
        
        # precompute valid choices for each pos

        options = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for num in range(1, n + 1):
                if (num % i == 0) or (i % num == 0):
                    options[i].append(num)
        print(options)


        # order by fewest available choices
        order = list(range(1, n + 1))
        order.sort(key = lambda i: len(options[i]))
        print(order)

        @lru_cache(None)
        def dfs(idx, used_mask):
            # idx : how many positions in order have we filled
            if idx == n:
                return 1
            
            pos = order[idx]
            total = 0
            for num in options[pos]:
                bit = 1 << (num - 1)
                if (used_mask & bit) == 0: # num unused
                    total += dfs(idx + 1, used_mask | bit)
            return total
            
        
        return dfs(0, 0)