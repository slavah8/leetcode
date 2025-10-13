class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        # dp[x] maximum earnings achieveable by the time you reach point x

        ends = defaultdict(list)
        for s, e, t in rides:
            ends[e].append((s, t))
        
        dp = [0] * (n + 1)

        for x in range(1, n + 1):
            
            best = dp[x - 1]

            for s, t in ends[x]:
                best = max(best, dp[s] + (x - s + t))
            
            dp[x] = best
        print(dp)
        return max(dp)