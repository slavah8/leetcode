class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @lru_cache(None)
        def dp(i, streak):
            # # i = how many posts painted so far
            # streak = 1 or 2 (how many same-color in a row at the end)
            if i == n:
                return 1

            ways = 0

            # choose same color
            if i > 0 and streak < 2:
                ways += dp(i + 1, streak + 1)
            

            if i == 0:
                # first post: k choices
                ways += dp(i + 1, 1) * k
            else:
                ways += dp(i + 1, 1) * (k - 1)
            
            return ways


        return dp(0, 1)