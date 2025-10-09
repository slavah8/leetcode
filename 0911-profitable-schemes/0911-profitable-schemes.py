class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        dp[i][people][p] =
        number of schemes using only crimes 0..i-1
        that use exactly 'people' members
        and achieve profit 'p' (where p is capped at minProfit)

        """

        MOD = 10 ** 9 + 7
        m = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1

        for i in range(1, m + 1):
            g = group[i - 1]
            w = profit[i - 1]

            for people in range(0, n + 1):
                for p in range(0, minProfit + 1):

                    ways = dp[i - 1][people][p]
                    if ways == 0:
                        continue
                    
                    dp[i][people][p] = (dp[i][people][p] + ways) % MOD

                    if people + g <= n:
                        p_new = min(minProfit, w + p)
                        dp[i][people + g][p_new] = (dp[i][people + g][p_new] + ways) % MOD
                        
        return sum(dp[m][people][minProfit] for people in range(n + 1)) % MOD
