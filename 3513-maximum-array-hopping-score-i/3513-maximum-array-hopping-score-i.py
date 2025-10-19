class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        # dp[:i] defined as max score you can get up to ith index

        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[1]

        for j in range(2, N):
            best = 0
            for i in range(j):
                score = (j - i) * nums[j]
                total = score + dp[i]
                if total > best:
                    best = total
            dp[j] = best
        
        return dp[N - 1]

            