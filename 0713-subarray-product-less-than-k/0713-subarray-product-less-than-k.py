class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        N = len(nums)
        if min(nums) >= k:
            return 0
        if k <= 0:
            return 0
        
        prod = 1
        count = 0
        for right in range(N):
            num = nums[right]
            prod *= num
            while left < N and prod >= k:
                num_left = nums[left]
                prod = prod // num_left
                left += 1
            count += (right - left + 1)
        return count
            
