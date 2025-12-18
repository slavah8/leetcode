class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        n = len(values)
        # dp[j] defined as the max score up to the jth index
        dp = [0] * n
        best_left = values[0] + 0
        # (values[i] + i) + (values[j] - j)
        # for each j just remember the best left 
        best = values[0]

        for j in range(1, n):
            
            dp[j] = best_left + (values[j] - j)
            best_left = max(best_left, values[j] + j)
            
            best = max(best, dp[j])
        print(dp)
        return best