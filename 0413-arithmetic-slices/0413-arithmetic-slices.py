class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        N = len(nums)
        start = 0
        ans = 0
        for i in range(2, N + 1):
            prev_diff = nums[i - 1] - nums[i - 2]
            if i < N:
                curr_diff = nums[i] - nums[i - 1]
                if curr_diff == prev_diff:
                    continue
            
            # streak breaks here
            L = i - start
            if L >= 3:
                ans += (L - 1) * (L - 2) // 2
            start = i - 1
        return ans

        

        
            
                
