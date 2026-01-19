class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        

        n = len(nums)
        cur_sum = 0
        best_pos = 0
        for x in nums:
            cur_sum += x
            if cur_sum < 0:
                cur_sum = 0
            best_pos = max(best_pos, cur_sum)
        
        best_neg = 0
        cur_sum = 0
        for x in nums:
            cur_sum += x
            if cur_sum > 0:
                cur_sum = 0
            
            best_neg = min(best_neg, cur_sum)
        
        print(best_neg)
        print(best_pos)
        best = max(abs(best_neg), abs(best_pos))
        return best
        
            

