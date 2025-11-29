class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            for j in range(0, i):
                if nums[j] <= nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        LIS = max(dp)
        return n - LIS

            

        
