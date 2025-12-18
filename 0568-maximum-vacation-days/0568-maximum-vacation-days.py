class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        # Let dp[w][c] = maximum vacation days you can still get starting on week w 
        # if you are in city c on Monday morning of that week.

        n = len(flights)
        k = len(days[0]) # k = weeks

        # dp[w][c] = max vacation days starting week w, being in city c on Monday
        dp = [[0] * n for _ in range(k + 1)]

        for w in range(k - 1, -1, -1):
            for c in range(n):
                # you can either stay
                best = days[c][w] + dp[w + 1][c]
                for nxt in range(n):
                    if flights[c][nxt] == 1:
                        best = max(best, dp[w + 1][nxt] + days[nxt][w])
                dp[w][c] = best
        
        return dp[0][0]
