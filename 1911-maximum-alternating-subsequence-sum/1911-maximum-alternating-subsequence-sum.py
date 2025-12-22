class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        INF = 10 ** 15
        n = len(nums)
        dp = [[-INF, -INF] for _ in range(n)]

        # dp[i][0] = best alternating sum using nums[0..i] where the subsequence ends with a + term
        dp[0][0] = nums[0] 
        # best alternating sum using nums[0..i] where the subsequence ends with a - term
        dp[0][1] = -INF

        for i in range(1, n):
            x = nums[i]
            # end with a +
            dp[i][0] = max(dp[i - 1][1] + x, dp[i - 1][0], x)

            # end with a - 
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - x)
        

        return dp[n - 1][0]