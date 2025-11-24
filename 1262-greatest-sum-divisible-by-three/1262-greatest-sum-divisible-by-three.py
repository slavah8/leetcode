class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        n = len(nums)
        INF = 10 ** 10
        # dp[i][r] max possible sum using up to i nums with remainder r
        dp = [[-INF] * 3 for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(1, n + 1):

            x = nums[i - 1]
            for r in range(3):
                # skip the curr num
                dp[i][r] = dp[i - 1][r]

            for r in range(3):
                # use the curr num, so now the rem changes
                if dp[i - 1][r] != -INF:
                    nr = (r + x) % 3
                    dp[i][nr] = max(dp[i][nr], dp[i - 1][r] + x) 
        print(dp)
        return dp[n][0]