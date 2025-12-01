class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # dp[x] = length of the longest square-streak that **ends** at value x
        
        vals = sorted(set(nums))
        present = set(vals)
        dp = {}
        best = 0
        for x in vals:
            y = int(math.isqrt(x))
            if y * y == x and y in dp:
                dp[x] = dp[y] + 1
            else:
                dp[x] = 1
            best = max(best, dp[x])
        
        return best if best >= 2 else -1
