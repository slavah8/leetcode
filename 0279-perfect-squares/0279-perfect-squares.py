class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1
        
        print(squares)
        INF = 10 ** 10
        dp = [INF] * (n + 1) # dp[x] : minimum number of squares to sum up to x 
        dp[0] = 0

        for x in range(1, n + 1):
            for sq in squares:
                if sq > x:
                    break
                dp[x] = min(dp[x], 1 + dp[x - sq])
        return dp[n]