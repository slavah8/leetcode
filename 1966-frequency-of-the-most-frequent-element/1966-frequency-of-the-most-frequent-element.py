class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        N = len(nums)

        best = 1
        L = 0
        total = 0
        for R in range(N):
            
            total += nums[R]
            while nums[R] * (R - L + 1) - total > k:
                total -= nums[L]
                L += 1
            best = max(best, R - L + 1)
        return best
             