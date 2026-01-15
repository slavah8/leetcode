class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        dp = [0] * n
        dp[0] = sum(i * nums[i] for i in range(n))

        best = dp[0]

        for k in range(1, n):
            moved = nums[n - k]
            dp[k] = dp[k - 1] + total - moved * n
            best = max(best, dp[k])
        
        return best