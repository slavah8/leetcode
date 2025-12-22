class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # Let dp[i] = minimum cost to cover travel days starting from index i

        n = len(days)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            day = days[i]

            j1 = bisect.bisect_right(days, day + 0)

            j7 = bisect.bisect_right(days, day + 6)

            j30 = bisect.bisect_right(days, day + 29)

            dp[i] = min(dp[j1] + costs[0], dp[j7] + costs[1], dp[j30] + costs[2])
        
        print(dp)
        return dp[0]

