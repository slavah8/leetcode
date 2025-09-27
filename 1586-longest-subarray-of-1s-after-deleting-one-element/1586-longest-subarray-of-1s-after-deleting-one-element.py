class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = 0
        best = 0
        zeroes_count = 0
        for right, x in enumerate(nums):
            if x == 0:
                zeroes_count += 1
            
            while zeroes_count > 1:
                left_num = nums[left]
                if left_num == 0:
                    zeroes_count -= 1
                left += 1
            
            best = max(best, right - left + 1)
        
        return best - 1

