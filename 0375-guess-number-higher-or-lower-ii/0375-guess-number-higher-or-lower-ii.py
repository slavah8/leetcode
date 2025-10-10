class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[L][R] = minimum money needed to guarantee a win if the secret number is in the inclusive range L, R

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        INF = 10 ** 20

        for length in range(1, n):
            for L in range(n - length + 1):
                R = L + length
                best = INF
                for x in range(L, R + 1):
                    left = dp[L][x - 1]  if x - 1 >= L else 0
                    right = dp[x + 1][R] if x + 1 <= R else 0

                    cost = x + max(left, right)
                    if cost < best:
                        best = cost
                dp[L][R] = 0 if best == INF else best
        
        return dp[1][n]
                    