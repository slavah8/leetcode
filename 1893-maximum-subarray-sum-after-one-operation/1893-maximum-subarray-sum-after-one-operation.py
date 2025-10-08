class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]**2
        # For each index i, track two best subarray sums ending at i:
        dp0 = nums[0]            # no square used, end at i
        # best sum ending at the current index i with the square already used once.
        dp1 = nums[0] * nums[0]  # square used exactly once, end at i
        ans = 0
        for x in nums[1:]:
            sq = x ** 2
            new_dp1 = max(dp1 + x, dp0 + sq, sq)
            dp0 = max(x, dp0 + x)
            dp1 = new_dp1
            ans = max(ans, dp1)
        return ans
        
