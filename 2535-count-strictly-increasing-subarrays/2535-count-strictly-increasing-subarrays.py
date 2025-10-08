class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        # dp[i] defined as number of subarrays up to index i

        N = len(nums)
        dp = [0] * N

        for i, x in enumerate(nums):
            if nums[i] > nums[i - 1]:
                dp[i] += dp[i - 1] + 1
            else:
                dp[i] = 1
        
        return sum(dp)


