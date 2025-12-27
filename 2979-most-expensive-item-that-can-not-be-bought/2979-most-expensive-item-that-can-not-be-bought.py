class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        
        a, b = primeOne, primeTwo

        limit = a * b

        dp = [False] * (limit + 1)

        dp[0] = True

        for x in range(1, limit + 1):
            ok = False
            if x - a >= 0 and dp[x - a]:
                ok = True
            
            if x - b >= 0 and dp[x - b]:
                ok = True
            
            dp[x] = ok
        
        ans = 0
        for x in range(1, limit + 1):
            if not dp[x]:
                ans = x
        
        return ans
            
