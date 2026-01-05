class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        print(suffix)

        # dp(i, M) = maximum number of stones the CURRENT player can collect
        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0
            
            if n - i <= 2 * M:
                return suffix[i]

            best = 0

            max_take = min(n - i, 2 * M)
            for X in range(1, max_take + 1):
                best = max(best, suffix[i] - dp(i + X, max(M, X)))
            return best
        
        return dp(0, 1)
        


