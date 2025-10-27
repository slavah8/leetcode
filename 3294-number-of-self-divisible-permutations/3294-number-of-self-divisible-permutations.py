class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        
        options = [[] for _ in range(n + 1)]

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a == 1

        for i in range(1, n + 1):
            for num in range(1, n + 1):
                if gcd(num, i):
                    options[i].append(num)
        print(options)

        order = list(range(1, n + 1))
        order.sort(key = lambda i: len(options[i]))
        print(order)

        @lru_cache(None)
        def dfs(idx, used_mask):
            # how many positions in order we have filled
            if idx == n:
                return 1

            pos = order[idx]
            total = 0
            for num in options[pos]:
                bit = 1 << (num - 1) # set the bit
                if (used_mask & bit) == 0:
                    total += dfs(idx + 1, used_mask | bit)
            return total

        return dfs(0, 0)
