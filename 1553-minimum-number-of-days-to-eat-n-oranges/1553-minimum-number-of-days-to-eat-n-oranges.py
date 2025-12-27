class Solution:
    def minDays(self, n: int) -> int:
        

        INF = 10 ** 10
        # dp(i) defined as minimum days to eat i oranges
        @lru_cache(None)
        def dp(i):

            if i <= 1:
                return i
            
            choice_2 = (i % 2) + 1 + dp(i // 2)
            choice_3 = (i % 3) + 1 +  dp(i // 3)
            
            return min(choice_2, choice_3)
            

        return dp(n)