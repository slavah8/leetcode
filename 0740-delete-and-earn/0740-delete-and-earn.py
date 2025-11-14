class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # points[x] = total points we get if we decide to use the value x
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        
        # dp[i] = max points you can earn considering numbers from 0 to i.
        dp = [0] * (max_val + 1)
        dp[1] = points[1]
        for i in range(2, max_val + 1):
            # take num i
        
            # skip num i
            dp[i] = max(dp[i - 1] if i - 1 >= 0 else 0, points[i] + dp[i - 2] if i - 2 >= 0 else 0)
        return dp[max_val]